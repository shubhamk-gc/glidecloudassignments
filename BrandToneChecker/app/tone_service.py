import uuid
from app.embeddings import get_embedding
from app.vector_db import collection
from app.llm import llm_review


def create_brand(brand_name, tone_keywords, samples):
    combined = " ".join(tone_keywords) + " " + " ".join(samples)
    embedding = get_embedding(combined)
    brand_id = str(uuid.uuid4())

    collection.add(
        ids=[brand_id],
        embeddings=[embedding],
        metadatas=[{
            "brand_id": brand_id,
            "brand_name": brand_name,
            "tone": ",".join(tone_keywords),
            "samples": " || ".join(samples)
        }]
    )
    return brand_id


def list_brands():
    data = collection.get(include=["metadatas"])
    names = set()
    for m in data["metadatas"]:
        if m:
            names.add(m["brand_name"])
    return list(names)


def get_brand(brand_name):
    res = collection.get(where={"brand_name": brand_name}, include=["metadatas"])
    if not res["metadatas"]:
        return None
    return res["metadatas"][0]


def check_tone(brand_name, text):
    query_emb = get_embedding(text)

    result = collection.query(
        query_embeddings=[query_emb],
        where={"brand_name": brand_name},
        n_results=1
    )

    score = 1 - result["distances"][0][0]
    meta = result["metadatas"][0][0]

    llm_output = llm_review(meta["tone"], text, score)

    return {
        "score": score,
        "tone": meta["tone"],
        "llm_result": llm_output
    }
