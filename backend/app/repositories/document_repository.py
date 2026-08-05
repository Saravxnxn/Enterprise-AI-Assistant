from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, document: Document):

        self.db.add(document)

        self.db.commit()

        self.db.refresh(document)

        return document

    def get_all(self):

        return self.db.query(Document).order_by(Document.upload_time.desc()).all()

    def get_by_id(
        self,
        document_id: int,
    ):

        return self.db.query(Document).filter(Document.id == document_id).first()

    def delete(
        self,
        document,
    ):

        self.db.delete(document)

        self.db.commit()

    def update_status(
        self,
        document,
        status: str,
    ):

        document.processing_status = status

        self.db.commit()

        self.db.refresh(document)

        return document

    def update_chunk_count(
        self,
        document,
        chunk_count: int,
    ):

        document.chunk_count = chunk_count

        self.db.commit()

        self.db.refresh(document)

        return document
