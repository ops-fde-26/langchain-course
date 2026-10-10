import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Load key-value pairs from the .env file into environment variables.
# That way the API key is not hardcoded in this file.
load_dotenv()


def main():
    # This is the raw text we will plug into the prompt later.
    information = (
        "Narendra Damodardas Modi is the Prime Minister of India. "
        "He has served as Prime Minister since May 2014 and previously "
        "was Chief Minister of Gujarat. He is a leader of the Bharatiya Janata Party (BJP)."
    )

    # A prompt template is a string with holes, written as {variable_name}.
    # LangChain fills those holes when you call invoke().
    # {information} is NOT Python f-string formatting here — it is a LangChain placeholder.
    summary_template = """
 given the infromation {information} about a person i want you to create:
 1. A short summary
 2. Two interesting facts about them
"""

    # PromptTemplate turns the string above into an object LangChain can chain.
    # input_variables must match the names inside { } in the template.
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    # ChatOpenAI is the chat model wrapper.
    # We still use the OpenAI client, but base_url sends requests to OpenRouter
    # so one API key can reach many models (here: openai/gpt-4o-mini).
    # temperature=0 => more factual / less random answers.
    llm = ChatOpenAI(
        model="openai/gpt-4o-mini",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        temperature=0,
    )

    # The | (pipe) builds a chain: output of the left step becomes input of the right.
    # Step 1: fill the prompt. Step 2: send that prompt to the LLM.
    # This is LCEL (LangChain Expression Language): prompt | model.
    chain = summary_prompt_template | llm

    # invoke() runs the whole chain once.
    # Pass a dict whose keys match input_variables ("information").
    # The LLM returns an AIMessage; .content is the text we care about.
    response = chain.invoke({"information": information})
    print(response.content)


# Run Python File / `python main.py` starts here.
# Without this, Python would only define main() and then exit.
if __name__ == "__main__":
    main()
