from src.embedding_model import create_embeddings
from src.chroma_client import get_collection
import os

def store_documents():
    file_path = os.path.join("data", "docs.txt")

    with open(file_path, "r", encoding="utf-8") as f:
        documents = [line.strip() for line in f.readlines() if line.strip()]

    print(f"📄 Loaded {len(documents)} documents")

    collection = get_collection()

    # OPTIONAL but recommended: clear old data
    if collection.count() > 0:
        collection.delete(ids=collection.get()["ids"])

    embeddings = create_embeddings(documents)

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=[f"doc_{i}" for i in range(len(documents))]
    )

    print(f"✅ Stored {len(documents)} documents")

if __name__ == "__main__":
    store_documents()
