from core.llm_converse import get_embeddings


def embed_text(text: str):
    return get_embeddings(text)
