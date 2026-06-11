# CodeAssist
User Input
    ↓
What type of source?
    ↓
 ┌────────────┬─────────────┬─────────┐
 │            │             │
PDF         URL          Plain Text
 │            │             │
 ↓            ↓             ↓
Loaders     Loaders      Text Loader
 │            │             │
 └────────────┴─────────────┘
              ↓
          Chunking
              ↓
         Embeddings
              ↓
         ChromaDB
              ↓
        Hybrid Search