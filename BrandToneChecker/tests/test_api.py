from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_flow():
    r = client.post("/brands", json={
        "tone_keywords": ["friendly"],
        "samples": ["We love our users"]
    })
    brand_id = r.json()["brand_id"]

    r2 = client.post("/check-tone", json={
        "brand_id": brand_id,
        "text": "We are pleased to serve you"
    })

    assert "score" in r2.json()
