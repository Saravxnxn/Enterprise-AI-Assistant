from sqlalchemy.orm import Session

from app.models.user import User


class AuthRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_user_by_username(
        self,
        username: str,
    ) -> User | None:

        return self.db.query(User).filter(User.username == username).first()

    def get_user_by_id(
        self,
        user_id: int,
    ) -> User | None:

        return self.db.query(User).filter(User.id == user_id).first()
