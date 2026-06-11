from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
# embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
def create_vector_store(chunks,collection_name="coding_mentor"):

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory = "./vectorstore",
        collection_name=collection_name

        
    )
    # vectorstore.persist()

    return vectorstore
# retriver

def get_retriever(collection_name="coding_mentor"):

    vectorstore = Chroma(
        persist_directory = "./vectorstore",     
        collection_name=collection_name,
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 5}
    )

    return retriever