import chromadb
from llama_index.core import VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

def query_system():
    # 1. Align configuration with your local models
    Settings.llm = Ollama(model="mistral", request_timeout=360.0)
    Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

    # 2. Re-connect to your persistent database
    db = chromadb.PersistentClient(path="./chroma_db")
    
    try:
        chroma_collection = db.get_collection("custom_rag_collection")
    except Exception:
        print("[!] Error: Vector collection not found. Please run 'python ingest.py' first.")
        return

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    
    # 3. Load the index straight from the DB (Skip re-embedding files!)
    index = VectorStoreIndex.from_vector_store(vector_store)
    
    # 4. Spin up the querying engine
    query_engine = index.as_query_engine(similarity_top_k=3)

    print("\n" + "="*50)
    print(" Local RAG System Ready (Powered by Mistral & Nomic)")
    print("="*50)

    while True:
        user_query = input("\nAsk a question (or type 'quit' to exit): ")
        if user_query.strip().lower() == 'quit':
            break
        if not user_query.strip():
            continue

        print("Searching context and generating answer...")
        try:
            response = query_engine.query(user_query)
            print("\n--- Answer ---")
            print(response)
        except Exception as e:
            print(f"\nAn error occurred during generation: {e}")

if __name__ == "__main__":
    query_system()