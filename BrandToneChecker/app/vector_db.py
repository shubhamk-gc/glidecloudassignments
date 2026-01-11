import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(
    name="brand_tones",
    metadata={"hnsw:space": "cosine"}
)
