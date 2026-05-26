STORE = []


def add_to_store(chunk, vec, metadata):
    STORE.append((chunk, vec, metadata))


def get_store():
    return STORE
