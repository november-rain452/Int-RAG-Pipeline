from embed import embed_text
from store import add_to_store
from chunk import chunk_text
from preprocess import clean_pdf, clean_markdown
from loaders.loader import load_documents


def ingest(directory: str):
    docs = load_documents(directory)

    for doc in docs:
        # preprocess
        if doc.type == "md":
            text = clean_markdown(doc.text)
        elif doc.type == "pdf":
            text = clean_pdf(doc.text)
        else:
            text = doc.text

        # chunk
        chunks = chunk_text(text)

        for chunk in chunks:
            vec = embed_text(chunk)
            add_to_store(chunk, vec, metadata={"source": doc.source, "type": doc.type})
