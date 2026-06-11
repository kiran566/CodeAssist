from rag.pdf_loader import load_pdf
from rag.hybrid_retriver import (
    create_hybrid_retriever
)

chunks = load_pdf(
    "uploads/binary_search _C.pdf"
)

retriever = create_hybrid_retriever(
    chunks
)

docs = retriever.invoke(
    "What is the time complexity of binary search?"
)

print("Retrieved:", len(docs))

for doc in docs:

    print("=" * 50)

    print(doc.page_content[:300])