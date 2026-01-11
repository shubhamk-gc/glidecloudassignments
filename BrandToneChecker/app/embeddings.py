import requests
from app.config import OLLAMA_BASE_URL, EMBED_MODEL

def get_embedding(text: str) -> list[float]:
    r = requests.post(
        f"{OLLAMA_BASE_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": text},
        timeout=60
    )
    r.raise_for_status()
    return r.json()["embedding"]
