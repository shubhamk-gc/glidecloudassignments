import json
from src.chroma_client import get_collection
from src.embedding_model import create_embeddings

CHUNK_SIZE = 300
JSON_PATH = "vectordb.json"

def chunk_text(text):
    return [text[i:i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]

def store_documents():
    with open("data/docs.txt", "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)
    embeddings = create_embeddings(chunks)

    collection = get_collection()

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"doc_{i}" for i in range(len(chunks))]
    )

    # 🔹 ALSO store in JSON (simple dump) my latest and final update
    json_data = []
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        json_data.append({
            "id": f"doc_{i}",
            "document": chunk,
            "embedding": emb
        })

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)

    print(f"✅ Stored {len(chunks)} chunks in ChromaDB")
    print(f"📄 Also stored vectors in {JSON_PATH}")

if __name__ == "__main__":
    store_documents()
