# query_engine.py

import os
from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI  # requires: pip install -U langchain-openai

# Set your OpenRouter API credentials
os.environ["OPENAI_API_KEY"] = "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"  # Replace with your real OpenRouter key
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# 1. Connect to SQLite DB
db = SQLDatabase.from_uri("sqlite:///zomato.db")

# 2. Define LLM from OpenRouter
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",  # You can also try "openai/gpt-3.5-turbo"
    temperature=0,
    max_tokens=256
)

# 3. Create the SQL Toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# 4. Initialize the SQL Agent
agent_executor = initialize_agent(
    tools=toolkit.get_tools(),
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True  # ✅ This helps avoid parsing failure
)


def run_chain(question: str):
    try:
        result = agent_executor.run(question)
        if not result:
            raise ValueError("Empty response from model.")
        return result
    except Exception as e:
        return f"❌ Agent failed: {e}"
