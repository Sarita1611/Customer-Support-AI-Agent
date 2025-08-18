from query_engine import run_chain

def main():
    print("🤖 Welcome to your Zomato Text-to-SQL AI Agent!")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ")
        if question.lower() == "exit":
            break
        try:
            answer = run_chain(question)
            print("Bot:", answer)
        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    main()
