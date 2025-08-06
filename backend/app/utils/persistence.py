"""

Handles saving and loading Q&A pairs to/from disk (e.g., saved.json).
Used by the chat route handlers.
"""


import os
import json

def load_data(path: str):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception:
        return []

def save_data(path: str, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
