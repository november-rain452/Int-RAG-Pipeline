from pathlib import Path
from md_loader import load_markdown
from pdf_loader import load_pdf
from schema.data_ingestion_schema import Document


def load_documents(directory: str) -> list[Document]:
    docs = []

    for file_path in Path(directory).glob("*"):
        if file_path.suffix.lower() == ".md":
            try:
                docs.append(load_markdown(str(file_path)))
            except Exception as e:
                print(f"Failed to load {file_path}: {e}")

        elif file_path.suffix.lower() == ".pdf":
            try:
                docs.append(load_pdf(str(file_path)))
            except Exception as e:
                print(f"Failed to load {file_path}: {e}")
        else:
            raise ValueError(f"Unsupported file type: {file_path}")

    return docs
