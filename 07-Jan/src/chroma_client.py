import chromadb
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)  # move out of src/
CHROMA_PATH = os.path.join(BASE_DIR, "chromadb")

_client = None

def get_collection():
    global _client

    if _client is None:
        _client = chromadb.PersistentClient(path=CHROMA_PATH)

    return _client.get_or_create_collection(
        name="docs_collection"
    )
