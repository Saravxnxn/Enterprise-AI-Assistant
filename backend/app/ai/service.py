from app.ai.router import ModelRouter


class AIService:

    def chat(self, messages: list):

        provider = ModelRouter.get_provider()

        return provider.generate_response(messages)
