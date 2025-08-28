import sys
from SQL_Agent import agent

def main():
    if len(sys.argv) < 2:
        print("Usage: PromptQL <your natural language request>")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    result = agent.run(query)
    print(result)

if __name__ == "__main__":
    main()
