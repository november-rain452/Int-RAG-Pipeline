from rag.vec_search import retrieve


def rag_tool(query: str) -> str:
    return retrieve(query)
