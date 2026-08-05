import httpx

from app.ai.providers.base_provider import BaseAIProvider
from app.core.config import settings


class OllamaProvider(BaseAIProvider):

    def generate_response(
        self,
        messages: list,
    ) -> dict:

        response = httpx.post(
            f"{settings.OLLAMA_BASE_URL}/api/chat",
            json={
                "model": settings.OLLAMA_MODEL,
                "messages": messages,
                "stream": False,
            },
            timeout=httpx.Timeout(300),
        )

        response.raise_for_status()

        data = response.json()

        return {
            "response": data["message"]["content"],
            "provider": "Ollama",
            "model": settings.OLLAMA_MODEL,
        }
