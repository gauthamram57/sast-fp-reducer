"""
Groq AI Provider
"""

import os

from dotenv import load_dotenv
from openai import OpenAI
from openai import APIError
from openai import RateLimitError

from src.ai.base import BaseAIClient

load_dotenv()


class GroqClient(BaseAIClient):
    """
    Groq implementation of the BaseAIClient interface.
    """

    def __init__(self):

        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = os.getenv("GROQ_MODEL")

        if not self.api_key:
            raise ValueError("GROQ_API_KEY is missing.")

        if not self.model:
            raise ValueError("GROQ_MODEL is missing.")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.groq.com/openai/v1",
            timeout=30,
        )

    def chat(self, prompt: str) -> str:

        print(f"[Groq] Using {self.model}")

        try:

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a Senior Application Security Engineer. "
                            "Return ONLY valid JSON."
                        ),
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                temperature=0,
            )

            return response.choices[0].message.content

        except RateLimitError as error:
            raise RuntimeError(
                f"Groq rate limit exceeded.\n{error}"
            )

        except APIError as error:
            raise RuntimeError(
                f"Groq API error.\n{error}"
            )
