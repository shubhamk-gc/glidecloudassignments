from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_flow():
    # Create brand
    r = client.post("/brands", json={
        "brand_name": "TestBrand",
        "tone_keywords": ["friendly"],
        "samples": ["We love our users"]
    })

    assert r.status_code == 200

    # Check tone using brand_name
    r2 = client.post("/check-tone", json={
        "brand_name": "TestBrand",
        "text": "We are pleased to serve you"
    })

    assert r2.status_code == 200
    data = r2.json()

    assert "score" in data
    assert "tone" in data
    assert "llm_result" in data
