from fastapi import FastAPI
from src.chroma_client import get_collection
from src.embedding_model import create_embeddings

app = FastAPI(title="08-Jan Vector Search")

SIMILARITY_THRESHOLD = 1.5

@app.post("/search")
def search(query: str):
    collection = get_collection()
    query_embedding = create_embeddings([query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    docs = results["documents"][0]
    distances = results["distances"][0]

    filtered = [
        {"document": d, "distance": dist}
        for d, dist in zip(docs, distances)
        if dist < SIMILARITY_THRESHOLD
    ]

    if not filtered:
        return {"query": query, "message": "No relevant document found"}

    return {"query": query, "results": filtered}
