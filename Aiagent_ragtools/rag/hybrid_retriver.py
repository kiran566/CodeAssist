from rag.vector_store import get_retriever
from rag.bm25_retriver import create_bm25_retriever


class HybridRetriever:
    def __init__(self, chunks):
        self.dense = get_retriever()
        self.bm25 = create_bm25_retriever(chunks)

    def invoke(self, query: str):

        dense_docs = self.dense.invoke(query)
        bm25_docs = self.bm25.invoke(query)

        all_docs = dense_docs + bm25_docs

        # remove duplicates
        seen = set()
        final_docs = []

        for doc in all_docs:
            if doc.page_content not in seen:
                seen.add(doc.page_content)
                final_docs.append(doc)

        return final_docs