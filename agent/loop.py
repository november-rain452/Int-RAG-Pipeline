from core.llm_converse import call_model
from parser import parse_response
from tools import rag_wrap_tool


def run_agent(query: str) -> str:
    for _ in range(5):
        response = call_model(query)
        parsed = parse_response(response)

        if parsed["action"] == "answer":
            print(parsed["data"])
            return

        elif parsed["rag_tool"]:
            context = rag_wrap_tool(parsed["data"])
            query = f"Context :\n {context}\n\n Question: {query}"
            continue
