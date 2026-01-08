from src.chroma_client import get_collection
from src.store_vectors import store_documents

def test_vectors_are_stored():
    store_documents()

    collection = get_collection()
    data = collection.get()

    assert len(data["ids"]) > 0, "No vectors stored in ChromaDB"
