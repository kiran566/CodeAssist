from langchain.retrievers import EnsembleRetriever

from rag.vector_store import get_retriever
from rag.bm25_retriver import create_bm25_retriever


def create_hybrid_retriever(chunks):

    chroma_retriever = get_retriever()

    bm25_retriever = create_bm25_retriever(
        chunks
    )

    hybrid = EnsembleRetriever(
        retrievers=[
            chroma_retriever,
            bm25_retriever
        ],

        weights=[0.4, 0.6]
    )

    return hybrid