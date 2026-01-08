import chromadb
import os

CHROMA_PATH = os.path.abspath("chromadb")
COLLECTION_NAME = "docs"

def get_collection():
    print("📦 Chroma persist dir:", CHROMA_PATH)

    client = chromadb.PersistentClient(
        path=CHROMA_PATH
    )

    return client.get_or_create_collection(
        name=COLLECTION_NAME
    )
