from app.repositories.conversation_repository import (
    ConversationRepository,
)


class ConversationService:

    def __init__(
        self,
        repository: ConversationRepository,
    ):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_conversation(
        self,
        conversation_id: int,
    ):
        return self.repository.get_by_id(conversation_id)

    def get_messages(
        self,
        conversation_id: int,
    ):
        return self.repository.get_messages(conversation_id)

    def rename(
        self,
        conversation,
        title: str,
    ):
        return self.repository.update_title(
            conversation,
            title,
        )

    def delete(
        self,
        conversation,
    ):
        self.repository.delete(conversation)
