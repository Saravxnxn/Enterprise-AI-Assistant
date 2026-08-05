from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.models.message import Message


class ConversationRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):

        stmt = select(Conversation).order_by(Conversation.updated_at.desc())

        return self.db.execute(stmt).scalars().all()

    def get_by_id(
        self,
        conversation_id: int,
    ):

        stmt = select(Conversation).where(Conversation.id == conversation_id)

        return self.db.execute(stmt).scalar_one_or_none()

    def get_messages(
        self,
        conversation_id: int,
    ):

        stmt = (
            select(Message)
            .where(Message.conversation_id == conversation_id)
            .order_by(Message.created_at.asc())
        )

        return self.db.execute(stmt).scalars().all()

    def update_title(
        self,
        conversation: Conversation,
        title: str,
    ):

        conversation.title = title

        self.db.commit()

        self.db.refresh(conversation)

        return conversation

    def delete(
        self,
        conversation: Conversation,
    ):

        self.db.delete(conversation)

        self.db.commit()
