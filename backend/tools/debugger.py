# tools/debugger.py

from langchain_core.tools import tool
from llm import llm


@tool
def debug_code(
    code: str,
    error_message: str = "",
    expected_behavior: str = ""
) -> str:
    """
    Analyze buggy code, explain errors, and suggest fixes.
    """

    prompt = f"""
    You are an expert programming mentor helping a student debug code.

    Code:
    {code}

    Error Message:
    {error_message if error_message else "Not provided"}

    Expected Behavior:
    {expected_behavior if expected_behavior else "Not provided"}

    Analyze the code and provide:

    1. Issue Type
       (Syntax Error / Runtime Error / Logic Error)

    2. Explanation
       Explain the issue in simple terms.

    3. Suggested Fix

    4. Corrected Code

    5. Time Complexity

    6. Space Complexity

    7. Tips to avoid similar mistakes in the future.
    """

    response = llm.invoke(prompt)

    return response.content