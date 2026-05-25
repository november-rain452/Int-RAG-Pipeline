import re


def clean_markdown(text: str) -> str:
    text = re.sub(r"```(.*?)```", r"\1", text, flags=re.DOTALL)
    text = re.sub(r"`(.*?)`", r"\1", text)
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    text = re.sub(r"\n\s*\n", "\n\n", text)
    return text.strip()


def clean_pdf(text: str) -> str:
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()
