from app.ai.providers.ollama_provider import OllamaProvider
from app.ai.providers.openai_provider import OpenAIProvider
from app.core.config import settings


class ModelRouter:

    @staticmethod
    def get_provider():

        provider = settings.MODEL_PROVIDER.lower()

        if provider == "ollama":
            return OllamaProvider()

        if provider == "openai":
            return OpenAIProvider()

        raise ValueError(f"Unsupported provider: {provider}")
