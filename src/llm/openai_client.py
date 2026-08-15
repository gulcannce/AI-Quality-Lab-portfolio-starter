
import os

from openai import OpenAI

from src.llm.client import LLMClient


class OpenAIClient(LLMClient):
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")

        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model="gpt-5-mini",
            input=prompt,
        )

        return response.output_text
    