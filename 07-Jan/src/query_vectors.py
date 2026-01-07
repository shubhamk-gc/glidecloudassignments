from src.chroma_client import get_collection
from src.embedding_model import create_embeddings

query = "What is Rag?"

collection = get_collection()

results = collection.query(
    query_embeddings=create_embeddings([query]),
    n_results=5,
    include=["documents", "distances"]
)

print("\nQuery:", query)
print("\nResults:")

documents = results.get("documents", [[]])[0]
distances = results.get("distances", [[]])[0]

if not documents:
    print("❌ No relevant documents found.")
else:
    for doc, dist in zip(documents, distances):
        print(f"\n📄 Document (distance={dist:.4f}):\n{doc}")
