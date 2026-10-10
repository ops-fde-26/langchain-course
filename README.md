# langchain-course

A small LangChain example: take notes about a person, fill a prompt template, send it to an LLM, print a summary and two facts.

Uses a Python **virtualenv** and **OpenRouter** (not uv).

## What you will learn

| Piece | What it does |
|--------|----------------|
| `PromptTemplate` | A prompt with a hole `{information}`. LangChain fills it when you run the chain. |
| `ChatOpenAI` | Chat model. `base_url` points at OpenRouter so one key can use many models. |
| `prompt \| llm` | A **chain** (LCEL): filled prompt goes into the model. |
| `invoke({...})` | Runs the chain once. `response.content` is the model's text. |

Code and comments: `main.py`.

## Setup

Python 3.11+ recommended.

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt
cp .env.example .env
```

Put your [OpenRouter](https://openrouter.ai/keys) key in `.env`:

```
OPENROUTER_API_KEY=your_key_here
```

Do not commit `.env` or `venv/`.

## Run

```bash
python main.py
```

In Cursor / VS Code: select interpreter `venv/Scripts/python.exe`, then Run Python File.

## Project files

```
main.py            prompt + model + chain
requirements.txt   pip packages
.env.example       copy to .env and add your key
```
