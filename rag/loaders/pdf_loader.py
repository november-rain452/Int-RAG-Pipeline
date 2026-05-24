import pymupdf


def load_pdf(file_path: str) -> dict:
    doc = pymupdf.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return {"text": text, "source": file_path, "type": "pdf"}
