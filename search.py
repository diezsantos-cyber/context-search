"""
Semantic search over code symbols using cosine similarity.
"""
import numpy as np
from typing import List, Dict
from embeddings import generate_embedding


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Compute cosine similarity between two vectors"""
    a_np = np.array(a)
    b_np = np.array(b)
    return np.dot(a_np, b_np) / (np.linalg.norm(a_np) * np.linalg.norm(b_np))


def search_symbols(query: str, symbols: List[Dict], top_k: int = 5) -> List[Dict]:
    """
    Search symbols by semantic similarity to query.
    Returns top_k most similar symbols.
    """
    # Generate query embedding
    query_embedding = generate_embedding(query)
    
    # Compute similarity for each symbol
    results = []
    for symbol in symbols:
        if 'embedding' not in symbol:
            continue
        
        similarity = cosine_similarity(query_embedding, symbol['embedding'])
        results.append({
            **symbol,
            'similarity': similarity
        })
    
    # Sort by similarity (descending)
    results.sort(key=lambda x: x['similarity'], reverse=True)
    
    return results[:top_k]
