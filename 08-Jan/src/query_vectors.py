from src.chroma_client import get_collection
from src.embedding_model import create_embeddings

THRESHOLD = 1.5  # similarity cutoff

def query_documents():
    query = input("Enter your query: ")

    collection = get_collection()
    query_embedding = create_embeddings([query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    documents = results["documents"][0]
    distances = results["distances"][0]

    relevant_docs = []

    for doc, dist in zip(documents, distances):
        if dist <= THRESHOLD:
            relevant_docs.append(doc)

    print("\n🔍 Search Results:")
    if not relevant_docs:
        print("No relevant document found")
    else:
        for i, doc in enumerate(relevant_docs, 1):
            print(f"\nResult {i}:\n{doc}")

if __name__ == "__main__":
    query_documents()
