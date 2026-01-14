from chromadb import PersistentClient

# Create persistent on-disk vector DB
client = PersistentClient(path="./chroma")

collection = client.get_or_create_collection(
    name="brand_tones",
    metadata={"hnsw:space": "cosine"}
)
