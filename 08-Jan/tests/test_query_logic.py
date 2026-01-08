from src.chroma_client import get_collection
from src.embedding_model import create_embeddings

SIMILARITY_THRESHOLD = 1.2

def test_query_returns_results():
    collection = get_collection()
    query_embedding = create_embeddings(["embeddings"])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    assert len(results["documents"][0]) > 0

def test_query_no_relevant_results_by_distance():
    collection = get_collection()
    query_embedding = create_embeddings(["completely unrelated text xyz"])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    distances = results["distances"][0]

    # All results should be above threshold → not relevant
    assert all(d > SIMILARITY_THRESHOLD for d in distances)
