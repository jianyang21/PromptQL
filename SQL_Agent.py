from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, Tool
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# --- LLM ---
llm = Ollama(model="llama3", temperature=0)

# --- SQL Prompt ---

sql_template = """
You are an expert SQL query generator.
The user will give you a request in plain English, and you must return ONLY a valid SQL query.
Do not add thoughts, explanations, or anything else.

Request: {user_request}
SQL:
"""

sql_prompt = PromptTemplate(input_variables=["user_request"], template=sql_template)
sql_chain = LLMChain(llm=llm, prompt=sql_prompt)

def generate_sql(user_request: str):
    return sql_chain.run(user_request=user_request)

# --- MongoDB Prompt ---
mongo_template = """
You are an expert MongoDB query generator.
The user will give you a request in plain English, and you must return a valid MongoDB query (in JSON/dict format).
Do not explain anything. Just return the query.

Request: {user_request}
MongoDB:
"""
mongo_prompt = PromptTemplate(input_variables=["user_request"], template=mongo_template)
mongo_chain = LLMChain(llm=llm, prompt=mongo_prompt)

def generate_mongo(user_request: str):
    return mongo_chain.run(user_request=user_request)

# --- Tools ---
sql_tool = Tool(
    name="SQL Query Generator",
    func=generate_sql,
    description="Use this to generate SQL queries from natural language."
)

mongo_tool = Tool(
    name="MongoDB Query Generator",
    func=generate_mongo,
    description="Use this to generate MongoDB queries from natural language."
)

# --- Agent ---
agent = initialize_agent(
    tools=[sql_tool, mongo_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True   # <--- important
)


# --- Example usage ---
query1 = "Give me the SQL command to count all users with salary above 3000"
query2 = "Give me the MongoDB query to count all users with salary above 3000"

print("SQL Output:", agent.run(query1))
print("MongoDB Output:", agent.run(query2))
