from rag.pdf_loader import load_pdf
from rag.bm25_retriver import create_bm25_retriever

chunks = load_pdf("uploads/binary_search _C.pdf")

bm25 = create_bm25_retriever(chunks)

docs = bm25.invoke(
    "middle = (first + last)/2"
)

print("Retrieved:", len(docs))

for doc in docs:

    print("=" * 50)

    print(doc.page_content[:300])