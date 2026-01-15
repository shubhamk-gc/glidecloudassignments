from chromadb import PersistentClient


client = PersistentClient(path="./chroma")

collection = client.get_or_create_collection(
    name="brand_tones",
    metadata={"hnsw:space": "cosine"}
)
