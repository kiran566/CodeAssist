from rag.pdf_loader import load_pdf
from rag.vector_store import create_vector_store

chunks = load_pdf(
    "uploads/binary_search _C.pdf"
)

vectorstore = create_vector_store(chunks,collection_name='binary_search')

print("PDF embedded successfully.")