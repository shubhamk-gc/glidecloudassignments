from src.chroma_client import get_collection

def debug():
    collection = get_collection()

    data = collection.get(include=["documents", "embeddings"])

    total = len(data["ids"])
    print(f"📦 Total vectors stored: {total}")

    if total == 0:
        print("❌ No vectors found")
        return

    print("\n📄 Sample document:")
    print(data["documents"][0])

    embedding = data["embeddings"][0]

    print("\n🔢 Embedding details:")
    print("• Dimension:", len(embedding))
    print("• First 10 values:", embedding[:10])

if __name__ == "__main__":
    debug()
