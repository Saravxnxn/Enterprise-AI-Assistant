from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import logger, setup_logging

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(api_router)

logger.info("Enterprise AI Assistant started successfully.")