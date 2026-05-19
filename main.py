from agent.loop import run_agent

if __name__ == "__main__":
    while True:
        query = input(">> ")
        run_agent(query)
