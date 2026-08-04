"""
Import every SQLAlchemy model here.

Alembic imports this file to discover models.
"""

from app.models.user import User

__all__ = [
    "User",
]
