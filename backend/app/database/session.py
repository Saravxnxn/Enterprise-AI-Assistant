from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

connection_string = (
    f"DRIVER={{{settings.DB_DRIVER}}};"
    f"SERVER={settings.DB_SERVER},{settings.DB_PORT};"
    f"DATABASE={settings.DB_NAME};"
    f"UID={settings.DB_USERNAME};"
    f"PWD={settings.DB_PASSWORD};"
    "TrustServerCertificate=yes;"
)

DATABASE_URL = (
    f"mssql+pyodbc:///?odbc_connect={quote_plus(connection_string)}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()