import openai

from app.ai.providers.base_provider import BaseAIProvider
from app.core.config import settings


class OpenAIProvider(BaseAIProvider):

    def __init__(self):
        self.client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.DEFAULT_MODEL

    def generate_response(
        self,
        prompt: str,
    ) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content or ""
