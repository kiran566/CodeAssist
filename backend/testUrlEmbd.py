# test_url_embeddings.py

from rag.url_loader import load_url
from rag.vector_store import create_vector_store

chunks = load_url(
    "https://neetcode.io/solutions/two-sum"
)

vectorstore = create_vector_store(
    chunks,
    collection_name="neetcode_two_sum"
)

print("URL embeddings created successfully.")