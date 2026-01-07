import ollama

def create_embeddings(texts):
    embeddings = []
    for text in texts:
        response = ollama.embeddings(
            model="llama3.2",
            prompt=text
        )
        embeddings.append(response["embedding"])
    return embeddings
