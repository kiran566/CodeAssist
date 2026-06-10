from langchain_core.tools import tool
from llm import llm


@tool
def analyze_complexity(code: str) -> str:
    """
    Analyze the time and space complexity of a code snippet.
    """

    prompt = f"""
    You are an expert in algorithms and data structures.

    Analyze the following code:

    {code}

    Return your answer in this format:

    Time Complexity:
    Space Complexity:

    Explanation:
    Explain step by step how the complexity was derived.

    Optimization:
    Suggest improvements if possible.
    """

    response = llm.invoke(prompt)

    return response.content