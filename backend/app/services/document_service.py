import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.ai.parsers.manager import ParserManager
from app.models.document import Document
from app.repositories.document_chunk_repository import (
    DocumentChunkRepository,
)
from app.repositories.document_content_repository import (
    DocumentContentRepository,
)
from app.repositories.document_embedding_repository import (
    DocumentEmbeddingRepository,
)
from app.repositories.document_repository import DocumentRepository
from app.services.document_chunk_service import (
    DocumentChunkService,
)
from app.services.document_content_service import (
    DocumentContentService,
)
from app.services.document_embedding_service import (
    DocumentEmbeddingService,
)


class DocumentService:

    ALLOWED_EXTENSIONS = {
        ".pdf",
        ".docx",
        ".xlsx",
        ".csv",
        ".txt",
        ".md",
    }

    UPLOAD_DIR = Path("uploads/documents")

    def __init__(
        self,
        repository: DocumentRepository,
    ):
        self.repository = repository

    def upload(
        self,
        file: UploadFile,
        user_id: int,
    ):

        extension = Path(file.filename).suffix.lower()

        if extension not in self.ALLOWED_EXTENSIONS:
            raise ValueError("Unsupported file type.")

        stored_filename = f"{uuid4()}{extension}"

        self.UPLOAD_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path = self.UPLOAD_DIR / stored_filename

        with open(
            file_path,
            "wb",
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer,
            )

        size = file_path.stat().st_size

        document = Document(
            original_filename=file.filename,
            stored_filename=stored_filename,
            file_type=extension,
            file_size=size,
            uploaded_by=user_id,
        )

        # Save metadata first
        document = self.repository.create(document)

        # Parse uploaded file
        content = ParserManager.parse(str(file_path))

        # Save extracted content
        content_service = DocumentContentService(
            DocumentContentRepository(self.repository.db)
        )

        content_service.save_content(
            document.id,
            content,
        )

        chunk_service = DocumentChunkService(
            DocumentChunkRepository(self.repository.db)
        )

        chunks = chunk_service.create_chunks(
            document.id,
            content,
        )

        self.repository.update_chunk_count(
            document,
            len(chunks),
        )

        self.repository.update_status(
            document,
            "CHUNKED",
        )

        embedding_service = DocumentEmbeddingService(
            DocumentEmbeddingRepository(self.repository.db)
        )

        embedding_service.create_embeddings(chunks)

        self.repository.update_embedding_info(
            document,
            model_name="all-MiniLM-L6-v2",
            vector_count=len(chunks),
        )

        self.repository.update_embedding_status(document)

        return document

    def list_documents(self):

        return self.repository.get_all()

    def get_document(
        self,
        document_id: int,
    ):

        return self.repository.get_by_id(document_id)

    def delete_document(
        self,
        document,
    ):

        file_path = self.UPLOAD_DIR / document.stored_filename

        if file_path.exists():
            file_path.unlink()

        self.repository.delete(document)
