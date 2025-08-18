from query_engine import get_text2sql_chain

def main():
    print("🤖 Welcome to your Text-to-SQL AI Agent (LangChain + SQLite)")
    print("Type 'exit' to quit.\n")

    run_chain = get_text2sql_chain()

    while True:
        query = input("You: ")
        if query.strip().lower() == 'exit':
            print("👋 Goodbye!")
            break

        result = run_chain(query)
        print(result)

if __name__ == "__main__":
    main()
