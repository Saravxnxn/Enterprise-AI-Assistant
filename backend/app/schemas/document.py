from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DocumentResponse(BaseModel):

    id: int

    original_filename: str

    stored_filename: str

    file_type: str

    file_size: int

    uploaded_by: int

    upload_time: datetime

    processing_status: str

    chunk_count: int | None = None

    embedding_model: str | None = None

    vector_count: int | None = None

    processed_time: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
