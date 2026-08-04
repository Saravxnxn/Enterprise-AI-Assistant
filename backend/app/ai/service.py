from app.ai.router import ModelRouter


class AIService:

    def chat(
        self,
        message: str,
    ):

        provider = ModelRouter.get_provider()

        return provider.generate_response(message)
