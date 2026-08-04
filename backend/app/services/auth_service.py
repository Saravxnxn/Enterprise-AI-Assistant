from fastapi import HTTPException, status

from app.authentication import JWTManager, PasswordHasher
from app.repositories.auth_repository import AuthRepository


class AuthService:

    def __init__(self, repository: AuthRepository):
        self.repository = repository

    def login(
        self,
        username: str,
        password: str,
    ):

        user = self.repository.get_user_by_username(username)

        if user is None:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )

        if not PasswordHasher.verify_password(
            password,
            user.password,
        ):

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )

        token = JWTManager.create_access_token({"sub": str(user.id)})

        return {
            "access_token": token,
            "token_type": "Bearer",
            "user": user,
        }
