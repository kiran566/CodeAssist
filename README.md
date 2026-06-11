# 🧠 AI Coding Mentor

An intelligent coding assistant built using **LangGraph**, **LangChain**, **Groq**, **Streamlit**, and **Hybrid RAG**. The system helps users solve coding problems, analyze complexity, debug code, and answer questions from uploaded PDFs or URLs.

---

## 📸 Application Preview


<p align="center">
  <img src="./Aiagent_ragtools/Photos/Screenshot (48).png" alt="AI Coding Mentor Screenshot" width="900"/>
</p>

---

## ✨ Features

- 🤖 **AI Coding Mentor**
  - Explains coding concepts
  - Answers programming questions
  - Provides interview preparation support

- 📄 **PDF-based RAG**
  - Upload coding notes or DSA PDFs
  - Ask questions grounded in the uploaded documents

- 🌐 **URL-based Knowledge Retrieval**
  - Load content from coding-related web pages
  - Convert them into searchable knowledge

- 🔍 **Hybrid Search**
  - Dense Retrieval using **Chroma + HuggingFace Embeddings**
  - Sparse Retrieval using **BM25**
  - Combines both for improved accuracy

- 🛠️ **Specialized Agent Tools**
  - Code Debugger
  - Time & Space Complexity Analyzer
  - Hint Generator
  - RAG Retriever Tool

- 🧠 **LangGraph Agent Workflow**
  - Determines when to answer directly
  - Decides when to invoke tools
  - Uses RAG only when additional context is required

- 💬 **Interactive Streamlit Interface**
  - Upload documents
  - Chat naturally with the assistant
  - Maintain conversation history

---

## 🏗️ Architecture

```text
                 ┌────────────────────┐
                 │   Streamlit UI     │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ LangGraph Agent    │
                 └─────────┬──────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
 │ Debug Tool  │   │ Hint Tool   │   │ Complexity  │
 └─────────────┘   └─────────────┘   │ Analyzer    │
                                     └──────┬──────┘
                                            │
                                            ▼
                                  ┌─────────────────┐
                                  │ Retriever Tool │
                                  └────────┬────────┘
                                           │
                              ┌────────────┴────────────┐
                              │                         │
                              ▼                         ▼
                    ┌────────────────┐      ┌────────────────┐
                    │ Chroma (Dense) │      │ BM25 (Sparse)  │
                    └────────────────┘      └────────────────┘
                              │                         │
                              └────────────┬────────────┘
                                           ▼
                                 ┌────────────────┐
                                 │  Groq LLM      │
                                 └────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### LLM & Agent Framework
- LangChain
- LangGraph
- Groq

### Retrieval-Augmented Generation (RAG)
- Chroma Vector Database
- HuggingFace Embeddings (`all-MiniLM-L6-v2`)
- BM25 Retriever

### Document Processing
- PyPDFLoader
- Web/URL Loader
- Recursive Character Text Splitter

---

## 📂 Project Structure

```text
CodeAssist/
│
├── main.py
├── graph.py
├── llm.py
├── state.py
│
├── rag/
│   ├── pdf_loader.py
│   ├── url_loader.py
│   ├── vector_store.py
│   ├── bm25_retriever.py
│   └── hybrid_retriever.py
│
├── tools/
│   ├── retrivertool.py
│   ├── debugger.py
│   ├── complexity.py
│   └── hints.py
│
├── uploads/
├── vectorstore/
├── screenshots/
│   └── ai-coding-mentor.png
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kiran566/CodeAssist.git
cd CodeAssist/Aiagent_ragtools
```

### 2. Install Dependencies

```bash
uv sync
```

### 3. Create Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### 4. Run the Application

```bash
streamlit run main.py
```

Open:

```text
http://localhost:8501
```

---

## 🎯 Future Enhancements

- Multi-document support
- Persistent user sessions
- Conversation summarization
- Code execution environment
- Cloud deployment

---

## 👨‍💻 Author

**Kiran**

This project was built to explore:

- Retrieval-Augmented Generation (RAG)
- AI Agents with LangGraph
- Hybrid Search Systems
- LLM-powered Developer Tools