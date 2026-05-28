def chunk_text(text: str, max_chars: int = 800, overlap_chars: int = 100) -> list[str]:
    words = text.split(" ")
    chunks = []

    current_words = []
    current_length = 0

    for word in words:
        # +1 accounts for the space we'll add when joining
        word_length = len(word) + 1

        if current_length + word_length <= max_chars:
            current_words.append(word)
            current_length += word_length
        else:
            # Commit the current chunk
            if current_words:
                chunks.append(" ".join(current_words).strip())

            # Form the overlap: look backward into current_words
            overlap_words = []
            overlap_len = 0
            for w in reversed(current_words):
                if overlap_len + len(w) + 1 <= overlap_chars:
                    overlap_words.insert(0, w)
                    overlap_len += len(w) + 1
                else:
                    break

            # Start the new chunk with the overlap + the current word
            current_words = overlap_words + [word]
            current_length = sum(len(w) + 1 for w in current_words)

    # Don't forget the last rolling chunk
    if current_words:
        chunks.append(" ".join(current_words).strip())

    return chunks
