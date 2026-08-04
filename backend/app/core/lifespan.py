from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("===========================================")
    logger.info("Enterprise AI Assistant Starting...")
    logger.info("===========================================")

    yield

    logger.info("===========================================")
    logger.info("Enterprise AI Assistant Stopped")
    logger.info("===========================================")