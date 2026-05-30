from core.llm_converse import call_model
from tools.rag_wrap_tool import rag_wrap_tool


def run_agent(query: str) -> None:
    rag_used = False
    context = ""
    original_question = query

    for _ in range(5):

        parsed = call_model(query)

        if parsed.action == "answer":
            print(parsed.data)
            return

        elif parsed.action == "rag_tool":

            if rag_used:
                print("Forcing final answer")

                query = f"""
                        You are a retrieval-based QA system.

                        You are NOT allowed to use any knowledge outside the provided context.

                        If the answer is not explicitly stated in the context, you MUST say:
                        "I do not have that information."

                        Context:
                        {context}

                        Question:
                        {original_question}

                        Answer:
                        """

                continue

            print("RAG CALLED")

            context = rag_wrap_tool(parsed.data)
            rag_used = True

            query = f"""
                    You have retrieved the following context.

                    You MUST now answer the question using ONLY this context.
                    DO NOT call rag_tool again.

                    If the answer is not present, say exactly:
                    "I do not have that information."

                    Context:
                    {context}

                    Question:
                    {original_question}
                    """
            continue

    print(" Max iterations reached. No answer produced.")
