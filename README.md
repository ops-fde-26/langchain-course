# langchain-course

Practice repo for LangChain. **Work happens on `main`.** When a lesson is ready to save:

1. Push `main`
2. Create / update a `chapter-NN-short-name` branch from that same commit
3. Add a row in the chapter table below
4. Expand **Concepts** for what that chapter teaches (this README is for ideas, `main.py` is for code)

## Chapters

| Chapter | Branch | Code (short) | Concepts |
|---------|--------|----------------|----------|
| 1 | `chapter-01-hello-world` | Person notes → prompt → LLM → print summary | PromptTemplate, ChatOpenAI, LCEL `\|`, invoke |

## How we work

- Build and run on **`main`**.
- Do not invent empty chapter branches. Branch only when that chapter’s code is on `main`.
- README: **minimal** “what the script does”, **detailed** “what LangChain idea this is”.

## Setup

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt
cp .env.example .env           # OPENROUTER_API_KEY=...
python main.py
```

Pick interpreter `venv/Scripts/python.exe` if you use Run Python File. Do not commit `.env` or `venv/`.

---

## Chapter 1 — hello world chain

**Code:** `main.py` takes a short paragraph about a person, fills `{information}` in a template, calls the model, prints the reply (summary + two facts).

### Concepts

**1. Prompt vs prompt template**  
A prompt is the final text the model sees. A **template** is that text with named holes: `{information}`. You write the instructions once. Each run you only pass new data.  
`{information}` is **not** a Python f-string. LangChain replaces it at `invoke()` time. If you used an f-string, the hole would be filled in Python *before* LangChain sees the template, and you would lose reuse and validation.

**2. `PromptTemplate`**  
Wraps the string and lists `input_variables` (here: `information`). Those names must match the `{...}` in the template and the keys in the dict you pass to `invoke`. If a variable is missing, LangChain errors **before** you pay for an LLM call.

**3. Chat model (`ChatOpenAI`)**  
The LLM is an object, not a raw HTTP call in `main`. We use the OpenAI-compatible client with `base_url=https://openrouter.ai/api/v1` so `OPENROUTER_API_KEY` can reach `openai/gpt-4o-mini` (and other models later by changing the `model` string).  
`temperature=0` makes answers more stable (good for “summarise these facts”). Higher temperature = more variety.

**4. Chain and the pipe `|` (LCEL)**  
`chain = summary_prompt_template | llm` means: output of the left step is input of the right.  
- Left: turn `{information: "..."}` into a full prompt.  
- Right: send that prompt to the model.  
You do not manually build a `messages=[...]` list. That composition is **LCEL** (LangChain Expression Language).

**5. `invoke`**  
`chain.invoke({"information": information})` runs the chain **once**, blocking until the full answer is back. The return value is an `AIMessage`. The usable text is `.content`.  
Later chapters can add `.stream()` (tokens as they arrive) or more steps in the pipe (`prompt | llm | parser`).

**6. Secrets**  
`load_dotenv()` reads `.env` into `os.environ`. The key stays off GitHub. Without it, `ChatOpenAI` cannot call the API.

**7. `if __name__ == "__main__"`**  
Run Python File executes the file as a script. It only *calls* `main()` if this block exists. Otherwise the file loads and exits.
