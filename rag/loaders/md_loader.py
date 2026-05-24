from pathlib import Path


def load_markdown(file_path: str) -> dict:
    text = Path(file_path).read_text(encoding="utf-8")
    return {"text": text, "source": file_path, "type": "md"}
