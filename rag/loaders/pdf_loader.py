import pymupdf
from pathlib import Path
from schema.data_ingestion_schema import Document


def load_pdf(file_path: str) -> Document:

    path = Path(file_path).resolve()

    if not path.exists():
        raise FileNotFoundError(f"{path} not found")

    with pymupdf.open(str(path)) as doc:
        text = ""

        for page in doc:
            text += page.get_text() + "\n\n"

    return Document(text=text, source=str(path), filename=path.name, type="pdf")
