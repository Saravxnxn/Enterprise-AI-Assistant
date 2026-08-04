from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class AuthRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_username(self, username: str) -> User | None:

        stmt = select(User).where(User.username == username)

        return self.db.execute(stmt).scalar_one_or_none()

    def get_by_id(self, user_id: int) -> User | None:

        stmt = select(User).where(User.id == user_id)

        return self.db.execute(stmt).scalar_one_or_none()
