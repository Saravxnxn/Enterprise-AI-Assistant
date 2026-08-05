from sqlalchemy.orm import Session

from app.models.document_chunk import DocumentChunk


class DocumentChunkRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create_many(
        self,
        chunks: list[DocumentChunk],
    ):

        self.db.add_all(chunks)

        self.db.commit()

        return chunks

    def get_by_document(
        self,
        document_id: int,
    ):

        return (
            self.db.query(DocumentChunk)
            .filter(DocumentChunk.document_id == document_id)
            .order_by(DocumentChunk.chunk_index)
            .all()
        )

    def get_by_ids(
        self,
        ids: list[int],
    ):

        return self.db.query(DocumentChunk).filter(DocumentChunk.id.in_(ids)).all()
