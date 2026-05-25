#!/usr/bin/env python3
"""
Proof of Concept: Index a Python file and search it.
Usage: python poc.py <file.py> <search_query>
"""
import sys
from pathlib import Path
from parser import CodeParser
from embeddings import embed_symbols
from search import search_symbols


def main():
    if len(sys.argv) < 3:
        print("Usage: python poc.py <file.py> <search_query>")
        print("Example: python poc.py example.py 'payment processing'")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    query = sys.argv[2]
    
    if not file_path.exists():
        print(f"Error: File {file_path} not found")
        sys.exit(1)
    
    # Read code
    code = file_path.read_text()
    
    print(f"📄 Parsing {file_path}...")
    
    # Extract symbols
    parser = CodeParser()
    symbols = parser.extract_symbols(code, "python")
    
    print(f"✅ Found {len(symbols)} symbols")
    
    # Generate embeddings
    print(f"🧠 Generating embeddings...")
    symbols = embed_symbols(symbols)
    
    # Search
    print(f"🔍 Searching for: '{query}'")
    results = search_symbols(query, symbols, top_k=5)
    
    print(f"\n📊 Top {len(results)} results:\n")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['type']} '{result['name']}' (line {result['line']}) - similarity: {result['similarity']:.3f}")
    

if __name__ == "__main__":
    main()
