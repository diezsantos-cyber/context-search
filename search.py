"""
Semantic search over code symbols using cosine similarity.
"""
from typing import List, Dict
try:
    from embeddings import generate_embedding
except:
    from embeddings_local import generate_embedding


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Compute cosine similarity between two vectors without numpy"""
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x * x for x in a) ** 0.5
    norm_b = sum(x * x for x in b) ** 0.5
    return dot_product / (norm_a * norm_b) if (norm_a * norm_b) > 0 else 0.0


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
