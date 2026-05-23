from rag.vec_search import retrieve


def rag_wrap_tool(query: str) -> str:
    return retrieve(query)
