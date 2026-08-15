from abc import ABC, abstractmethod


class LLMClient(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate an LLM response for a prompt."""
        raise NotImplementedError
