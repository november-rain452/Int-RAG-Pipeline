from agent.loop import run_agent
from rag.ingest import ingest

if __name__ == "__main__":

    ingest("data/")

    while True:
        query = input(">> ")
        run_agent(query)
