from rag.vector_store import get_retriever

retriever = get_retriever()

docs = retriever.invoke(
    "Explain binary search"
)

print("Retrieved:", len(docs))

for doc in docs:
    print("=" * 50)
    print(doc.page_content[:300])