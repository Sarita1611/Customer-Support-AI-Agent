import os
from dotenv import load_dotenv
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_huggingface import HuggingFaceEndpoint

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable

# Load environment variables
load_dotenv()

def get_text2sql_chain():
    # Read environment variables
    hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    db_uri = os.getenv("DB_URI")

    if not hf_token or not db_uri:
        raise EnvironmentError("Check .env file for Hugging Face token or DB URI.")

    # Hugging Face LLM
    llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    temperature=0.2,
    max_new_tokens=512,
)


    # SQLite database connection
    db = SQLDatabase.from_uri(db_uri)

    # Prompt template
    template = """
    Based on the following table schema, write an SQL query that answers the user's question.

    Schema:
    {schema}

    Question: {question}

    SQL Query:
    """
    prompt = PromptTemplate.from_template(template)

    # LangChain Runnable Pipeline
    chain: Runnable = (
        {"schema": lambda _: db.get_table_info(), "question": lambda x: x["question"]}
        | prompt
        | llm
        | StrOutputParser()
    )

    # Function that returns SQL + results
    def run_chain(question: str):
        sql_query = chain.invoke({"question": question})
        try:
            result = db.run(sql_query)
            return f"🔍 SQL:\n{sql_query}\n\n📊 Result:\n{result}"
        except Exception as e:
            return f"⚠️ Error executing SQL:\n{sql_query}\n\n{str(e)}"

    return run_chain
