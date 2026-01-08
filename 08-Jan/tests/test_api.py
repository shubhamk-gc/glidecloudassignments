from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_search_endpoint_success():
    response = client.post("/search", params={"query": "embeddings"})
    assert response.status_code == 200

    data = response.json()
    assert "results" in data
    assert len(data["results"]) > 0

def test_search_endpoint_no_results():
    response = client.post("/search", params={"query": "blockchain"})
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert data["message"] == "No relevant document found"
