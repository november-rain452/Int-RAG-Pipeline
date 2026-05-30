from .preprocess import split_paragraphs


def chunk_text(text: str, max_chars: int = 1000, overlap_chars: int = 200) -> list[str]:

    paragraphs = split_paragraphs(text)
    if not paragraphs:
        return []

    chunks = []
    current_chunk = ""
    current_len = 0

    for para in paragraphs:
        para_len = len(para)

        # if size of para bigger than limit :append current chunk
        if current_chunk and current_len + para_len > max_chars:

            chunks.append(current_chunk.strip())
            # Start a new chunk with overlap: keep the last `overlap_chars` characters
            if overlap_chars > 0 and len(current_chunk) > overlap_chars:
                current_chunk = current_chunk[-overlap_chars:] + "\n\n" + para
            else:
                current_chunk = para
            current_len = len(current_chunk)
        else:
            # Add to current chunk (with a paragraph break if not empty)
            if current_chunk:
                current_chunk += "\n\n" + para
            else:
                current_chunk = para
            current_len = len(current_chunk)

    # last chunk
    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks
