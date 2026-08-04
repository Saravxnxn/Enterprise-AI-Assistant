from fastapi import HTTPException, status

from app.authentication import JWTManager, PasswordHasher
from app.core.constants import USER_STATUS_ACTIVE
from app.repositories.auth_repository import AuthRepository
from app.schemas.auth import UserResponse


class AuthService:

    def __init__(self, repository: AuthRepository):
        self.repository = repository

    def login(
        self,
        username: str,
        password: str,
    ):

        user = self.repository.get_by_username(username)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )

        if user.status != USER_STATUS_ACTIVE:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User account is inactive",
            )

        if not PasswordHasher.verify_password(
            password,
            user.password,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )

        access_token = JWTManager.create_access_token({"sub": str(user.id)})

        return {
            "access_token": access_token,
            "token_type": "Bearer",
            "user": UserResponse.model_validate(user),
        }
