import streamlit as st
import asyncio
import nest_asyncio
asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
nest_asyncio.apply()
import chromadb
import os
from llama_index.core import VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.core.retrievers import QueryFusionRetriever
from llama_index.postprocessor.flag_embedding_reranker import FlagEmbeddingReranker

try:
    import transformers
    from transformers import PreTrainedTokenizerBase

    def prepare_for_model_custom(
        self,
        ids,
        pair_ids=None,
        add_special_tokens=True,
        padding=False,
        truncation=False,
        max_length=None,
        **kwargs
    ):
        bos_id = self.bos_token_id if self.bos_token_id is not None else 0
        eos_id = self.eos_token_id if self.eos_token_id is not None else 2
        
        if truncation and max_length is not None:
            overhead = 4 if pair_ids is not None else 2
            if len(ids) + (len(pair_ids) if pair_ids is not None else 0) + overhead > max_length:
                if pair_ids is not None:
                    max_pair_len = max_length - overhead - len(ids)
                    if max_pair_len > 0:
                        pair_ids = pair_ids[:max_pair_len]
                    else:
                        pair_ids = []
                        ids = ids[:max_length - overhead]
                else:
                    ids = ids[:max_length - overhead]
                    
        if pair_ids is not None:
            input_ids = [bos_id] + ids + [eos_id, eos_id] + pair_ids + [eos_id]
        else:
            input_ids = [bos_id] + ids + [eos_id]
            
        return {
            "input_ids": input_ids,
            "attention_mask": [1] * len(input_ids)
        }
        
    PreTrainedTokenizerBase.prepare_for_model = prepare_for_model_custom
except Exception as patch_err:
    st.warning(f"Failed to apply tokenizer monkey patch: {patch_err}")

# Ensure root data directory exists
BASE_DATA_DIR = "./data"
os.makedirs(BASE_DATA_DIR, exist_ok=True)

# --- Page Configuration ---
st.set_page_config(page_title="Enterprise RAG Core", page_icon="🛡️", layout="wide")

# --- Custom Styling ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    html, body, [class*="css"], .stMarkdown { font-family: 'Inter', sans-serif; }
    .main-title {
        background: linear-gradient(90deg, #10b981, #3b82f6);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-size: 2.3rem; font-weight: 800; display: inline-block; margin-bottom: 0.1rem;
    }
    .subheader-text { font-size: 0.95rem; color: #64748b; margin-bottom: 1.5rem; }
    .sidebar-section { background: rgba(128, 128, 128, 0.04); border: 1px solid rgba(128, 128, 128, 0.1); border-radius: 8px; padding: 12px; margin-bottom: 12px; }
    .sidebar-section-title { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; color: #94a3b8; margin-bottom: 6px; }
    .citation-header { font-size: 0.82rem; font-weight: 600; color: #3b82f6; margin-bottom: 2px; }
    .citation-preview { font-size: 0.82rem; color: #475569; background: rgba(128, 128, 128, 0.02); border-left: 3px solid #10b981; padding: 8px; border-radius: 0 4px 4px 0; margin-bottom: 10px; }
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_resource
def get_reranker():
    return FlagEmbeddingReranker(
        model="BAAI/bge-reranker-base", 
        top_n=3,
        use_fp16=False
    )

# --- Initialize RAG Components ---
@st.cache_resource
def load_advanced_rag_engine(collection_name, update_version=0):
    Settings.llm = Ollama(model="mistral", request_timeout=360.0)
    Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

    db = chromadb.PersistentClient(path="./chroma_db")
    try:
        chroma_collection = db.get_collection(collection_name)
    except Exception:
        return None

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    index = VectorStoreIndex.from_vector_store(vector_store)
    
    # 1. Hybrid Search Configuration (Vector + BM25)
    vector_retriever = index.as_retriever(similarity_top_k=5)
    
    # Building BM25 keyword parser from raw storage nodes
    try:
        results = chroma_collection.get()
        if not results or not results.get("ids"):
            return None
        
        from llama_index.core.schema import TextNode
        all_nodes = []
        for doc, meta, doc_id in zip(results.get("documents", []), results.get("metadatas", []), results.get("ids", [])):
            node = TextNode(
                text=doc,
                id_=doc_id,
                metadata={
                    "file_name": meta.get("file_name", "Unknown Document"),
                    "page_label": meta.get("page_label", "N/A"),
                }
            )
            all_nodes.append(node)
    except Exception as e:
        st.warning(f"Error loading collection nodes: {e}")
        return None

    if not all_nodes:
        return None

    bm25_retriever = BM25Retriever.from_defaults(nodes=all_nodes, similarity_top_k=5)
    
    # Fusing retrievers using Reciprocal Rank Fusion (RRF)
    hybrid_retriever = QueryFusionRetriever(
        [vector_retriever, bm25_retriever],
        similarity_top_k=6,
        num_queries=1, # Keep 1 to disable slow LLM query generation cycles locally
        mode="reciprocal_rerank"
    )
    
    # 2. Local Cross-Encoder Reranker Setup
    local_reranker = get_reranker()
    
    # Assemble comprehensive query execution pipeline
    from llama_index.core.query_engine import RetrieverQueryEngine
    return RetrieverQueryEngine.from_args(
        retriever=hybrid_retriever,
        node_postprocessors=[local_reranker]
    )

# --- Sidebar Control Center ---
with st.sidebar:
    st.markdown("### 🛡️ System Control Center")
    st.markdown("<hr style='margin: 8px 0;'>", unsafe_allow_html=True)
    
    # Feature 1: Multi-Collection Selection / Creation
    st.markdown('<div class="sidebar-section-title">Database Namespace</div>', unsafe_allow_html=True)
    db_client = chromadb.PersistentClient(path="./chroma_db")
    existing_collections = [c.name for c in db_client.list_collections()]
    
    if not existing_collections:
        existing_collections = ["default_knowledge_base"]
        
    selected_collection = st.selectbox("Active Collection", existing_collections)
    
    new_col_name = st.text_input("➕ Create New Collection Name")
    if st.button("Initialize Namespace", use_container_width=True):
        if new_col_name.strip():
            clean_name = "".join([c for c in new_col_name.replace(" ", "_") if c.isalnum() or c=="_"])
            db_client.get_or_create_collection(clean_name)
            os.makedirs(f"{BASE_DATA_DIR}/{clean_name}", exist_ok=True)
            st.success(f"Namespace '{clean_name}' created!")
            st.rerun()

    # Active target specific uploads directory configuration 
    active_upload_dir = f"{BASE_DATA_DIR}/{selected_collection}"
    os.makedirs(active_upload_dir, exist_ok=True)

    # Feature 2: Document Drag-and-Drop
    st.markdown('<div class="sidebar-section-title">Upload Documents</div>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader("Drop files", type=["pdf", "txt"], accept_multiple_files=True, label_visibility="collapsed")
    
    if uploaded_files:
        triggered = False
        for file in uploaded_files:
            file_path = os.path.join(active_upload_dir, file.name)
            if not os.path.exists(file_path):
                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())
                triggered = True
        if triggered:
            with st.spinner("Processing advanced hybrid index parsing..."):
                from ingest import initialize_ingestion
                if initialize_ingestion(selected_collection):
                    st.session_state["update_version"] = st.session_state.get("update_version", 0) + 1
                    st.rerun()

    # Feature 3: Clear Chat Button
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🗑️ Clear Conversational Memory", use_container_width=True):
        if "messages" in st.session_state:
            del st.session_state["messages"]
        st.rerun()

# --- Main App Core Interaction ---
st.markdown("<div class='main-title'>Advanced Hybrid RAG Core</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subheader-text'>Target Collection: <b>{selected_collection}</b> | Pipeline: BM25 + Vector Dense Search + BGE Reranking</div>", unsafe_allow_html=True)

# Initialize session state cache-buster
if "update_version" not in st.session_state:
    st.session_state["update_version"] = 0

query_engine = load_advanced_rag_engine(selected_collection, update_version=st.session_state["update_version"])

if query_engine is None:
    st.info("👋 This workspace namespace is empty. Drop files in the sidebar panel to seed documents.")
    st.stop()

# Conversation State Management
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": f"System active on database context partition: **{selected_collection}**. How can I assist you?", "sources": None}]

# Render History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if msg.get("sources"):
            with st.expander("🔍 Verified Retrieval Context Source Nodes"):
                for idx, src in enumerate(msg["sources"]):
                    st.markdown(f"<div class='citation-header'>Source {idx+1}: {src['file_name']} (Page {src['page_label']}) | Relative Match Rerank Score: {src['score']:.4f}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='citation-preview'>{src['text']}</div>", unsafe_allow_html=True)

# User Query Processing Interaction Loop
if user_query := st.chat_input("Ask a question matching context parameters..."):
    st.session_state.messages.append({"role": "user", "content": user_query, "sources": None})
    with st.chat_message("user"):
        st.write(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Executing hybrid semantic matching & cross-encoder optimization..."):
            try:
                response = query_engine.query(user_query)
                answer = str(response)
                
                source_nodes_data = []
                if hasattr(response, "source_nodes") and response.source_nodes:
                    for node in response.source_nodes:
                        metadata = node.node.metadata
                        source_nodes_data.append({
                            "file_name": metadata.get("file_name", "Unknown Document"),
                            "page_label": metadata.get("page_label", "N/A"),
                            "text": node.node.get_content(),
                            "score": getattr(node, "score", 0.0) # Evaluated cross-encoder output score
                        })
                
                st.write(answer)
                
                if source_nodes_data:
                    with st.expander("🔍 Verified Retrieval Context Source Nodes"):
                        for idx, src in enumerate(source_nodes_data):
                            st.markdown(f"<div class='citation-header'>Source {idx+1}: {src['file_name']} (Page {src['page_label']}) | Relative Match Rerank Score: {src['score']:.4f}</div>", unsafe_allow_html=True)
                            st.markdown(f"<div class='citation-preview'>{src['text']}</div>", unsafe_allow_html=True)
                            
                st.session_state.messages.append({"role": "assistant", "content": answer, "sources": source_nodes_data if source_nodes_data else None})
            except Exception as e:
                st.error(f"Execution Error: {e}")