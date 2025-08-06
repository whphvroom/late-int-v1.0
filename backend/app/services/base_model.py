"""

Defines a common interface (BaseModelClient) for integrating various model backends.
Each model client must implement this interface to ensure consistency.
"""

from abc import ABC, abstractmethod

class BaseModelClient(ABC):
    @abstractmethod
    def chat(self, message: str, max_tokens: int = 300) -> str:
        pass
