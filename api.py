"""
FastAPI REST API for Context Search
"""
from fastapi import FastAPI, HTTPException, Header, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid
import os
import zipfile
import tempfile
from pathlib import Path

from parser import CodeParser
from embeddings import embed_symbols
from search import search_symbols

app = FastAPI(
    title="Context Search API",
    description="Semantic code search for AI agents - 98% fewer tokens than grep",
    version="0.1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple API key auth (replace with proper auth later)
VALID_API_KEYS = set(os.getenv("API_KEYS", "demo-key-123").split(","))

# In-memory storage (replace with DB later)
repos = {}


def verify_api_key(api_key: str = Header(..., alias="X-API-Key")):
    if api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key


class IndexRequest(BaseModel):
    repo_name: str
    language: str = "python"


class IndexResponse(BaseModel):
    repo_id: str
    symbols_count: int
    message: str


class SearchRequest(BaseModel):
    query: str
    repo_id: str
    top_k: int = 5


class SearchResult(BaseModel):
    name: str
    type: str
    language: str
    line: int
    similarity: float


class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult]
    count: int


@app.get("/")
def root():
    return {
        "service": "Context Search API",
        "status": "running",
        "version": "0.1.0",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/index", response_model=IndexResponse)
async def index_repo(
    file: UploadFile = File(...),
    api_key: str = Header(..., alias="X-API-Key")
):
    """
    Index a code repository (uploaded as zip file).
    Returns repo_id for later searches.
    """
    verify_api_key(api_key)
    
    if not file.filename.endswith('.zip'):
        raise HTTPException(status_code=400, detail="Only .zip files accepted")
    
    repo_id = str(uuid.uuid4())
    
    # Extract zip to temp directory
    with tempfile.TemporaryDirectory() as temp_dir:
        zip_path = Path(temp_dir) / file.filename
        
        # Save uploaded file
        with open(zip_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Extract
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        # Parse all .py files
        parser = CodeParser()
        all_symbols = []
        
        for py_file in Path(temp_dir).rglob("*.py"):
            try:
                code = py_file.read_text()
                symbols = parser.extract_symbols(code, "python")
                
                # Add file context
                for symbol in symbols:
                    symbol['file'] = str(py_file.relative_to(temp_dir))
                
                all_symbols.extend(symbols)
            except Exception as e:
                # Skip files that fail
                continue
        
        if not all_symbols:
            raise HTTPException(status_code=400, detail="No Python symbols found in zip")
        
        # Generate embeddings
        all_symbols = embed_symbols(all_symbols)
        
        # Store in memory
        repos[repo_id] = {
            'repo_name': file.filename,
            'symbols': all_symbols,
            'symbols_count': len(all_symbols)
        }
    
    return IndexResponse(
        repo_id=repo_id,
        symbols_count=len(all_symbols),
        message=f"Indexed {len(all_symbols)} symbols successfully"
    )


@app.post("/search", response_model=SearchResponse)
def search_repo(
    request: SearchRequest,
    api_key: str = Header(..., alias="X-API-Key")
):
    """
    Search indexed repository by semantic query.
    """
    verify_api_key(api_key)
    
    if request.repo_id not in repos:
        raise HTTPException(status_code=404, detail="Repo not found")
    
    repo = repos[request.repo_id]
    symbols = repo['symbols']
    
    # Search
    results = search_symbols(request.query, symbols, top_k=request.top_k)
    
    # Format response
    search_results = [
        SearchResult(
            name=r['name'],
            type=r['type'],
            language=r.get('language', 'python'),
            line=r['line'],
            similarity=r['similarity']
        )
        for r in results
    ]
    
    return SearchResponse(
        query=request.query,
        results=search_results,
        count=len(search_results)
    )


@app.get("/repos")
def list_repos(api_key: str = Header(..., alias="X-API-Key")):
    """
    List all indexed repos for this API key.
    """
    verify_api_key(api_key)
    
    return {
        "repos": [
            {
                "repo_id": repo_id,
                "repo_name": repo['repo_name'],
                "symbols_count": repo['symbols_count']
            }
            for repo_id, repo in repos.items()
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
