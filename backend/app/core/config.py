from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    PROJECT_DESCRIPTION: str
    PROJECT_AUTHOR: str

    ENVIRONMENT: str

    HOST: str
    PORT: int

    LOG_LEVEL: str

    API_V1_PREFIX: str
    DB_SERVER: str
    DB_PORT: int
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_DRIVER: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()