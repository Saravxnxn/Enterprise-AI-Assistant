from datetime import UTC, datetime, timedelta

from jose import jwt

from app.core.config import settings


class JWTManager:

    @staticmethod
    def create_access_token(
        data: dict,
    ) -> str:

        payload = data.copy()

        expire = datetime.now(UTC) + timedelta(
            minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )

        payload.update({"exp": expire})

        return jwt.encode(
            payload,
            settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM,
        )

    @staticmethod
    def decode_token(
        token: str,
    ) -> dict:

        return jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )
