"""
Generate embeddings for code symbols using local model (sentence-transformers).
Fallback when OpenAI API unavailable.
"""
from typing import List, Dict
from sentence_transformers import SentenceTransformer

# Load lightweight model
model = SentenceTransformer('all-MiniLM-L6-v2')  # 80MB, fast


def generate_embedding(text: str) -> List[float]:
    """Generate embedding using local model"""
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding.tolist()


def embed_symbols(symbols: List[Dict]) -> List[Dict]:
    """
    Add embeddings to each symbol.
    Creates embedding from: name + type + surrounding context
    """
    for symbol in symbols:
        # Create text for embedding
        embed_text = f"{symbol['type']}: {symbol['name']}"
        if 'docstring' in symbol and symbol['docstring']:
            embed_text += f"\n{symbol['docstring']}"
        
        symbol['embedding'] = generate_embedding(embed_text)
    
    return symbols
