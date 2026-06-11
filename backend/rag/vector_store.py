from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
# embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
def create_vector_store(chunks,collection_name):

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./vectorstore",
        collection_name=collection_name

        
    )

    return vectorstore