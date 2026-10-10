# langchain-course

LangChain practice repo. Each **chapter is a git branch**. Checkout the chapter you are on, then run `main.py`.

| Chapter | Branch | What you build |
|---------|--------|----------------|
| 1 | `chapter-01-hello-world` | `PromptTemplate` + `ChatOpenAI` + a chain (`prompt \| llm`) |
| 2 | *(not started)* | Next lesson — new branch when you begin it |

`main` stays in sync with the latest finished chapter.

## Chapter 1 — hello world chain

Take notes about a person, fill a prompt template, send it to an LLM, print a short summary and two facts.

| Piece | What it does |
|--------|----------------|
| `PromptTemplate` | A prompt with a hole `{information}`. LangChain fills it when you run the chain. |
| `ChatOpenAI` | Chat model. `base_url` points at OpenRouter so one key can use many models. |
| `prompt \| llm` | A **chain** (LCEL): filled prompt goes into the model. |
| `invoke({...})` | Runs the chain once. `response.content` is the model's text. |

Code and comments: `main.py`.

```bash
git checkout chapter-01-hello-world
```

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
