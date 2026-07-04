# Week 7 — Advanced Hybrid RAG Core with BM25 & BGE Reranking

A high-performance local Retrieval-Augmented Generation (RAG) system built with **Streamlit**, **LlamaIndex**, **ChromaDB**, **Ollama**, and **BAAI/bge-reranker-base** for fast and highly accurate semantic retrieval.

## System Architecture & Pipeline

```mermaid
graph TD
    A[User Query] --> B[Hybrid Retriever]
    B --> C[Vector Dense Search (Ollama nomic-embed-text)]
    B --> D[Sparse Keyword Search (BM25 Retriever)]
    C --> E[Reciprocal Rank Fusion - RRF]
    D --> E
    E --> F[Top-6 Candidate Nodes]
    F --> G[Cross-Encoder Reranker (BAAI/bge-reranker-base)]
    G --> H[Top-3 Re-ordered Nodes]
    H --> I[LLM Response Synthesis (Ollama Mistral)]
    I --> J[Streamlit Chat UI]
```

1. **Namespace & Collection Management**: Multi-collection workspace namespaces (collections) implemented in ChromaDB.
2. **Dense Embeddings & Vector Storage**: Utilizes Ollama's local `nomic-embed-text` embedding model to embed chunks and stores them in a local persistent Chroma DB.
3. **Sparse BM25 Search**: To ensure exact-match and keyword retrieval robustness, database documents are reconstructed into in-memory `TextNode` objects dynamically to feed a local BM25 keyword retriever.
4. **Reciprocal Rank Fusion (RRF)**: Fuses candidate nodes from dense vector search and sparse BM25 keyword search using RRF.
5. **Cross-Encoder Reranking**: Re-orders the top candidate chunks using `BAAI/bge-reranker-base` to ensure only the most relevant contexts are fed into the LLM context window.
6. **Response Generation**: Generates high-fidelity answers using Ollama's local `mistral` LLM.

---

## Performance & Cache Optimizations

1. **Lightweight Node Reconstruction**:
   Directly parses nodes from the database client metadata instead of heavy JSON deserialization (`TextNode.from_json`), resulting in a **13,000x initialization speedup** (~54 seconds down to 0.004 seconds).
2. **Optimized Cross-Encoder Selection**:
   Upgraded the Reranker model from the slow `bge-reranker-large` to `bge-reranker-base` (278M parameters), providing near-equivalent ranking precision with significantly faster loading times.
3. **Session Cache-Busting**:
   Utilizes an `update_version` session state cache buster instead of calling `st.cache_resource.clear()`. This allows newly uploaded documents to be index-parsed and queried immediately without purging heavy model weights and network clients from RAM.
4. **Transformers v5.x Compatibility**:
   Incorporates a dynamic monkey-patch for the deprecated `prepare_for_model` method of Hugging Face tokenizers, ensuring seamless operation on the latest systems.

---

## File Structure

```
week7_Avi_Mathur/
├── app.py                # Main Streamlit application and query execution UI
├── ingest.py             # Document loading, parsing, and embedding ingestion
├── query.py              # CLI query verification script
├── rag_pipeline.py       # Custom pipeline utilities
├── requirements.txt      # Dependency specification
└── README.md             # This file
```

---

## Getting Started

### 1. Prerequisites
- Install **Ollama** and fetch the embedding/LLM models:
  ```bash
  ollama pull mistral
  ollama pull nomic-embed-text
  ```

### 2. Installation
Navigate to this directory and install Python dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the Streamlit server locally:
```bash
streamlit run app.py
```
This will launch the Web UI on `http://localhost:8501`.
