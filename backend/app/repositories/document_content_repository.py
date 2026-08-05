from sqlalchemy.orm import Session

from app.models.document_content import DocumentContent


class DocumentContentRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        document_content: DocumentContent,
    ):

        self.db.add(document_content)

        self.db.commit()

        self.db.refresh(document_content)

        return document_content

    def get_by_document_id(
        self,
        document_id: int,
    ):

        return (
            self.db.query(DocumentContent)
            .filter(DocumentContent.document_id == document_id)
            .first()
        )
