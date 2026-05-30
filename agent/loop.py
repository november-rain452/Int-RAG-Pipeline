from core.llm_converse import call_model
from tools.rag_wrap_tool import rag_wrap_tool


def run_agent(query: str) -> None:
    original_query = query
    for _ in range(5):
        parsed = call_model(query)

        if parsed.action == "answer":
            print(parsed.data)
            return parsed.data

        elif parsed.action == "rag_tool":
            rag_response = rag_wrap_tool(original_query)
            query = f""" You are an AI assistant
            User query: {original_query}
            Retrieved context : {rag_response}
            Rules:
            - If the context answers the query, return:
            {{"action": "answer", "data": "..."}}
            - Otherwise, return:
            {{"action": "answer", "data": "I do not know the answer to that query"}}
            """
    return "I do not know the answer to that query"
