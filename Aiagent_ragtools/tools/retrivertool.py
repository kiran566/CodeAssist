from langchain.tools import tool
from rag.hybrid_retriver import HybridRetriever

_hybrid = None


def init_retriever(chunks):
    global _hybrid
    _hybrid = HybridRetriever(chunks)


@tool
def retrieve_context(query: str):
    """
    Retrieve relevant context from uploaded PDF using Hybrid RAG (dense + BM25 search).
    """

    if _hybrid is None:
        return "No documents indexed yet."

    docs = _hybrid.invoke(query)

    return "\n\n".join(d.page_content[:300] for d in docs)