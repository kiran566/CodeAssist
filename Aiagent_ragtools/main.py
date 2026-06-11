import streamlit as st
from langchain_core.messages import HumanMessage
import os
import shutil

from graph import graph
from rag.pdf_loader import load_pdf
from rag.vector_store import create_vector_store
from tools.retrivertool import init_retriever   # 🔥 IMPORTANT FIX

# ----------------------------
# UI CONFIG
# ----------------------------
st.set_page_config(page_title="AI Coding Mentor", layout="wide")
st.title("🧠 AI Coding Mentor (Agent + Hybrid RAG + Tools)")

# ----------------------------
# SESSION STATE
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# SHOW CHAT HISTORY
# ----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ----------------------------
# PDF UPLOAD
# ----------------------------
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(uploaded_file, f)

    st.success("PDF uploaded successfully")

    # ----------------------------
    # LOAD + CHUNK
    # ----------------------------
    chunks = load_pdf(file_path)

    st.info(f"Chunks created: {len(chunks)}")

    # ----------------------------
    # VECTOR STORE (CHROMA)
    # ----------------------------
    create_vector_store(chunks)

    # ----------------------------
    # INIT HYBRID RETRIEVER (🔥 IMPORTANT FIX)
    # ----------------------------
    init_retriever(chunks)

    st.success("RAG system ready (Chroma + BM25)")

# ----------------------------
# CHAT HISTORY DISPLAY
# ----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ----------------------------
# USER INPUT
# ----------------------------
user_input = st.chat_input("Ask anything (PDF / LeetCode / Debug / DS Algo)...")

if user_input:

    # show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # ----------------------------
    # CALL LANGGRAPH AGENT
    # ----------------------------
    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=user_input)
            ]
        },
        config={
            "configurable": {
                "thread_id": "streamlit-user"
            }
        }
    )

    response = result["messages"][-1].content

    # show assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)