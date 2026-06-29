"""
OpenRouter AI client with automatic model fallback.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI
from openai import APIError
from openai import RateLimitError

load_dotenv()


class OpenRouterClient:

    def __init__(self):

        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.base_url = os.getenv("OPENROUTER_BASE_URL")

        models = os.getenv("OPENROUTER_MODELS", "")
        self.models = [
            model.strip()
            for model in models.split(",")
            if model.strip()
        ]

        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY missing.")

        if not self.models:
            raise ValueError("OPENROUTER_MODELS missing.")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
            timeout=30,
        )

    def chat(self, prompt: str) -> str:

        last_error = None

        for model in self.models:

            print(f"Trying model: {model}")

            try:

                response = self.client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a Senior Application "
                                "Security Engineer. "
                                "Always return valid JSON."
                            ),
                        },
                        {
                            "role": "user",
                            "content": prompt,
                        },
                    ],
                    temperature=0,
                )

                print(f"✓ Success using {model}")

                return response.choices[0].message.content

            except RateLimitError as error:

                print(f"⚠ Rate limited: {model}")

                last_error = error

                continue

            except APIError as error:

                print(f"⚠ API Error on {model}")

                last_error = error

                continue

        raise RuntimeError(
            f"All configured models failed.\n{last_error}"
        )
