"""

Implements the BaseModelClient interface for OpenAI's API (e.g., GPT-4o).
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
from app.services.base_model import BaseModelClient

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIClient(BaseModelClient):
    def chat(self, message: str, max_tokens: int = 300) -> str:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": message}],
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
