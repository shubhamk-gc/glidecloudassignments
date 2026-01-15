from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_brand():
    response = client.post("/brands", json={
        "brand_name": "Nike",
        "tone_keywords": ["bold", "motivational", "confident"],
        "samples": [
            "Just do it",
            "Push your limits",
            "Greatness is earned"
        ]
    })

    assert response.status_code == 200
    data = response.json()
    assert "brand_id" in data
    assert isinstance(data["brand_id"], str)
