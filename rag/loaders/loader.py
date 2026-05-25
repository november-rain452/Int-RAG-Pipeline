from pathlib import Path
from md_loader import load_markdown
from pdf_loader import load_pdf
from schema.data_ingestion_schema import Document


def load_documents(directory: str) -> list[Document]:
    docs = []

    for file_path in Path(directory).glob("*"):
        if file_path.suffix == ".md":
            docs.append(load_markdown(str(file_path)))
        elif file_path.suffix == ".pdf":
            docs.append(load_pdf(str(file_path)))

    return docs
