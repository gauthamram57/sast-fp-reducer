"""
Utility functions for parsing LLM responses.
"""

import json
import re


def extract_json(text: str) -> dict:
    """
    Extract JSON from an LLM response.

    Supports:
    - Pure JSON
    - Markdown code blocks
    - Extra explanatory text
    """

    text = text.strip()

    # Case 1: already valid JSON
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Case 2: JSON inside ```json ... ```
    match = re.search(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL)

    if match:
        return json.loads(match.group(1))

    # Case 3: First {...} block
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:
        return json.loads(match.group(0))

    raise ValueError("No valid JSON found in model response.")
