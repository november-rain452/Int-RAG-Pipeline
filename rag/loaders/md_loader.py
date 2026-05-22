from pathlib import Path


def load_markdown_files(directory: str):
    docs = []

    for file_path in Path(directory).glob("*.md"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        docs.append({"text": text, "source": str(file_path)})

    return docs
