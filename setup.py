from setuptools import setup, find_packages

setup(
    name="PromptQL",
    version="0.1",
    py_modules=["cli", "SQL_Agent"],
    install_requires=[
        "langchain",
        "langchain-community",
        "ollama",
    ],
    entry_points={
        "console_scripts": [
            "PromptQL=cli:main",
        ],
    },
)
