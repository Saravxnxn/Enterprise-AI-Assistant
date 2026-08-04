from abc import ABC, abstractmethod


class BaseAIProvider(ABC):

    @abstractmethod
    def generate_response(
        self,
        prompt: str,
    ) -> str:
        pass
