from app.ai.providers.openai_provider import OpenAIProvider


class ModelRouter:

    @staticmethod
    def get_provider():

        return OpenAIProvider()
