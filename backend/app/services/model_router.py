"""

Delegates requests to the appropriate model client for specified functions
"""

from app.services.openai_client import OpenAIClient

def get_model(speed_mode: bool = False):
    return OpenAIClient()
