from rag.pdf_loader import load_pdf
from rag.vector_store import create_vector_store

chunks = load_pdf("uploads/binary_search _C.pdf")

print("Chunks:", len(chunks))

try:
    vectorstore = create_vector_store(chunks)

    print("Collection:", vectorstore._collection.name)
    print("Count:", vectorstore._collection.count())

except Exception as e:
    print(type(e))
    print(e)
    raise