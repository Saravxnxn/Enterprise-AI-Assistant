from app.models.document_content import DocumentContent
from app.repositories.document_content_repository import (
    DocumentContentRepository,
)


class DocumentContentService:

    def __init__(
        self,
        repository: DocumentContentRepository,
    ):
        self.repository = repository

    def save_content(
        self,
        document_id: int,
        content: str,
    ):

        document_content = DocumentContent(
            document_id=document_id,
            content=content,
        )

        return self.repository.create(document_content)
