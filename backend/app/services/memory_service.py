from app.repositories.memory_repository import MemoryRepository


class MemoryService:

    def __init__(
        self,
        repository: MemoryRepository,
    ):
        self.repository = repository

    def get_or_create_conversation(
        self,
        conversation_id: int | None,
        user_id: int,
    ):

        if conversation_id:

            conversation = self.repository.get_conversation(conversation_id)

            if conversation:
                return conversation

        return self.repository.create_conversation(
            title="New Conversation",
            user_id=user_id,
        )

    def save_user_message(
        self,
        conversation_id: int,
        message: str,
    ):

        return self.repository.save_message(
            conversation_id,
            "user",
            message,
        )

    def save_ai_message(
        self,
        conversation_id: int,
        message: str,
    ):

        return self.repository.save_message(
            conversation_id,
            "assistant",
            message,
        )

    def load_history(
        self,
        conversation_id: int,
    ):

        return self.repository.get_messages(conversation_id)
