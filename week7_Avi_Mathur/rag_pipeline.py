import os
import chromadb
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.node_parser import SentenceSplitter

Settings.llm = Ollama(model="mistral", request_timeout=360.0)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")
Settings.text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=50)

db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("custom_rag_collection")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
print("Loading documents...")
documents = SimpleDirectoryReader("./data").load_data()
print("Building the index... (This takes a moment on the first run)")
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
)
query_engine = index.as_query_engine()
user_query = "What is the main idea of the document?"
print(f"\nUser Question: {user_query}")
print("Thinking...")
response = query_engine.query(user_query)
print("\n--- Generated Answer ---")
print(response)