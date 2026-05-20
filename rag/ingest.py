from embed import embed_text
from store import add_to_store
from chunk import chunk_text


def ingest(text: str):
    chunks = chunk_text(text)
    for chunk in chunks:
        vec = embed_text(chunk)
        add_to_store(chunk, vec)
