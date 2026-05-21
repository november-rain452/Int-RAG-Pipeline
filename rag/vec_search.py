from embed import embed_text
from store import get_store
from utils.similarity import cosine_similarity


def retrieve(query: str, top_k=3):
    query_vec = embed_text(query)
    store = get_store()

    scores = []

    for chunk, vec in store:
        score = cosine_similarity(query_vec, vec)
        scores.append((score, chunk))

    scores.sort(reverse=True)
    return "\n".join(text for _, text in scores[:top_k])
