from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.core.logging import logger
from app.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("===========================================")
    logger.info("Enterprise AI Assistant Starting...")
    logger.info("===========================================")

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        logger.info("SQL Server connection established successfully.")

    except Exception as ex:
        logger.exception("Database connection failed.")
        raise ex

    yield

    logger.info("===========================================")
    logger.info("Enterprise AI Assistant Stopped")
    logger.info("===========================================")
