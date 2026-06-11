import os
from rag.pdf_loader import load_pdf

path = "uploads/binary_search _C.pdf"

print("Current Directory:", os.getcwd())
print("Exists:", os.path.exists(path))

chunks = load_pdf(path)

print("Total Chunks:", len(chunks))