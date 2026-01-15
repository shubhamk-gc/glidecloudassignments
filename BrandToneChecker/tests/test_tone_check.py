from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_full_tone_flow():
    # Create brand
    create = client.post("/brands", json={
        "brand_name": "Apple",
        "tone_keywords": ["clean", "minimal", "premium"],
        "samples": [
            "Designed for simplicity",
            "Premium performance",
            "Beautiful technology"
        ]
    })

    assert create.status_code == 200

    # Check tone using brand_name
    check = client.post("/check-tone", json={
        "brand_name": "Apple",
        "text": "This phone delivers premium performance with beautiful design"
    })

    assert check.status_code == 200
    data = check.json()

    assert "score" in data
    assert "tone" in data
    assert "llm_result" in data
