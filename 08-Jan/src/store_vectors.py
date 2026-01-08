from src.chroma_client import get_collection
from src.embedding_model import create_embeddings

CHUNK_SIZE = 300

def chunk_text(text):
    return [text[i:i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]

def store_documents():
    with open("data/docs.txt", "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)
    embeddings = create_embeddings(chunks)

    collection = get_collection()

    # 🔥 CLEAR EXISTING DATA SAFELY
    existing = collection.get()["ids"]
    if existing:
        collection.delete(ids=existing)

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"doc_{i}" for i in range(len(chunks))]
    )

    print(f"✅ Stored {len(chunks)} chunks in ChromaDB")

if __name__ == "__main__":
    store_documents()
