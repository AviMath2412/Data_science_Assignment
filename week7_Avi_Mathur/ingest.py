import os
import chromadb
from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex, Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.node_parser import SentenceSplitter

def initialize_ingestion(collection_name="custom_rag_collection"):
    print("Initializing embedding model...")
    Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")
    Settings.text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=50)

    print(f"Setting up local ChromaDB storage for collection: '{collection_name}'...")
    db = chromadb.PersistentClient(path="./chroma_db")
    
    # Dynamically select or build unique isolated data paths
    chroma_collection = db.get_or_create_collection(collection_name)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    target_dir = f"./data/{collection_name}"
    if not os.path.exists(target_dir) or not os.listdir(target_dir):
        print(f"\n[!] Error: '{target_dir}' folder is empty.")
        return False

    print(f"Loading documents from {target_dir} ...")
    documents = SimpleDirectoryReader(target_dir).load_data()

    print("Building and saving vector index...")
    VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
    )
    print(f"Successfully indexed data into collection '{collection_name}'!")
    return True

if __name__ == "__main__":
    initialize_ingestion()