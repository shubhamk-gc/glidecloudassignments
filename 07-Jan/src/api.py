from fastapi import FastAPI
from src.chroma_client import get_collection
from src.embedding_model import create_embeddings

app = FastAPI(title="07-Jan Vector Search")

@app.post("/search")
def search(query: str):
    collection = get_collection()

    query_embedding = create_embeddings([query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    return {
        "query": query,
        "results": results["documents"][0]
    }
