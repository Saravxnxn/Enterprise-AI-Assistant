from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.models.message import Message


class MemoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_conversation(
        self,
        title: str,
        user_id: int,
    ) -> Conversation:

        conversation = Conversation(
            title=title,
            user_id=user_id,
        )

        self.db.add(conversation)
        self.db.commit()
        self.db.refresh(conversation)

        return conversation

    def get_conversation(
        self,
        conversation_id: int,
    ) -> Conversation | None:

        stmt = select(Conversation).where(Conversation.id == conversation_id)

        return self.db.execute(stmt).scalar_one_or_none()

    def save_message(
        self,
        conversation_id: int,
        role: str,
        content: str,
    ) -> Message:

        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content,
        )

        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)

        return message

    def get_messages(
        self,
        conversation_id: int,
        limit: int = 20,
    ) -> list[Message]:

        stmt = (
            select(Message)
            .where(Message.conversation_id == conversation_id)
            .order_by(Message.created_at.asc())
        )

        return list(self.db.execute(stmt).scalars().all())[-limit:]
