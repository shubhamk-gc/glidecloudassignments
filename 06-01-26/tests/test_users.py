import os
os.environ["ENV"] = "test"


import pytest
from fastapi.testclient import TestClient
from main import app
from database import users_collection

# Set test environment
os.environ["ENV"] = "test"

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_db():
    """Clear database before each test"""
    users_collection.delete_many({})
    yield
    users_collection.delete_many({})


def test_health_check():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json()["message"] == "FastAPI is running"



def test_create_user():
    payload = {
        "name": "Test User",
        "age": 25,
        "email": "test@example.com"
    }

    response = client.post("/api/users", json=payload)
    assert response.status_code == 200
    assert "id" in response.json()


def test_get_users():
    client.post("/api/users", json={
        "name": "User One",
        "age": 22,
        "email": "one@example.com"
    })

    response = client.get("/api/users")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_user_by_id():
    create_res = client.post("/api/users", json={
        "name": "User Two",
        "age": 30,
        "email": "two@example.com"
    })

    user_id = create_res.json()["id"]
    response = client.get(f"/api/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "User Two"


def test_update_user():
    create_res = client.post("/api/users", json={
        "name": "User Three",
        "age": 28,
        "email": "three@example.com"
    })

    user_id = create_res.json()["id"]

    update_res = client.put(
        f"/api/users/{user_id}",
        json={"age": 35}
    )

    assert update_res.status_code == 200
    assert update_res.json()["message"] == "User updated successfully"


def test_delete_user():
    create_res = client.post("/api/users", json={
        "name": "User Four",
        "age": 40,
        "email": "four@example.com"
    })

    user_id = create_res.json()["id"]

    delete_res = client.delete(f"/api/users/{user_id}")
    assert delete_res.status_code == 200

    get_res = client.get(f"/api/users/{user_id}")
    assert get_res.status_code == 404
