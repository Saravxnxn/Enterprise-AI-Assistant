from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    stored_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    file_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    file_size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    uploaded_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    upload_time: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    processing_status: Mapped[str] = mapped_column(
        String(20),
        default="UPLOADED",
    )

    chunk_count: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    embedding_model: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    vector_count: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    processed_time: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )
