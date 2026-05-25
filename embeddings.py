"""
Generate embeddings for code symbols using OpenAI.
"""
import os
from openai import OpenAI
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_embedding(text: str) -> List[float]:
    """Generate embedding for a single text using ada-003"""
    response = client.embeddings.create(
        model="text-embedding-ada-002",  # Using ada-002 (ada-003 not yet released)
        input=text
    )
    return response.data[0].embedding


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
