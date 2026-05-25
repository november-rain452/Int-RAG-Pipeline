from pathlib import Path
from schema.data_ingestion_schema import Document


def load_markdown(file_path: str) -> Document:

    path = Path(file_path).resolve()

    if not path.exists():
        raise FileNotFoundError(f"{path} not found")

    text = path.read_text(encoding="utf-8")

    return Document(text=text, source=str(path), filename=path.name, type="md")


def load_markdown_files(directory: str):
    docs = []

    for file_path in Path(directory).glob("*.md"):
        docs.append(load_markdown(str(file_path)))

    return docs
