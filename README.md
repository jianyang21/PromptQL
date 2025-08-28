# PromptQL – Natural Language to SQL/NoSQL AI Agent  

PromptQL is an AI-powered agent that runs locally and converts natural language queries into executable SQL or NoSQL code.  

Instead of manually writing database queries, you can type what you want in plain English, and PromptQL will generate the corresponding database command.  

## Features  
- Runs offline without external APIs  
- Translates natural language into SQL and NoSQL queries  
- Works with relational databases (MySQL, PostgreSQL, SQLite) and NoSQL databases (MongoDB)  
- Command-line interface for interaction  
- Easy to extend and customize  

## Repository Structure  

PromptQL/
├── sql-agent.py # Core NLP to SQL/NoSQL logic
├── cli.py # Command-line interface
├── setup.py # Installation script
└── README.md # Documentation


## Installation

Clone the repository and install dependencies:

git clone https://github.com/jianyang21/PromptQL.git
cd PromptQL
pip install -r requirements.txt
Usage
1. Create and activate a virtual environment
Windows

# Windows
py -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate


Go to Command Prompt
pip install -e .

Run the CLI Tool
PromptQL "Show me all employees earning more than 5000"

Example SQL Output
SELECT * FROM employees WHERE salary > 5000;


Example NoSQL Output
{ "salary": { "$gt": 5000 } }


Tech Stack
1. Python 3.10+
2. NLP models
3. LangChain and/or Ollama (optional) for enhanced query parsing
4. SQL and NoSQL dialect support
