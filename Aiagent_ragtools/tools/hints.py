from langchain_core.tools import tool

from llm import llm


@tool
def give_hint(problem: str) -> str:
    """
    Provide progressive hints for solving coding problems.
    Do not reveal the complete solution immediately.
    """

    prompt = f"""
    You are an expert coding mentor.

    A student is solving this problem:

    {problem}

    Provide:

    1. Hint 1 (very subtle)
    2. Hint 2 (slightly stronger)
    3. Approach (high-level idea)

    Do NOT provide code.
    Do NOT reveal the final answer.
    """

    response = llm.invoke(prompt)

    return response.content