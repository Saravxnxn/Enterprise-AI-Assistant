from sqlalchemy.orm import Session

from app.models.document_embedding import DocumentEmbedding


class DocumentEmbeddingRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create_many(
        self,
        embeddings: list[DocumentEmbedding],
    ):

        self.db.add_all(embeddings)

        self.db.commit()

        return embeddings

    def get_by_chunk(
        self,
        chunk_id: int,
    ):

        return (
            self.db.query(DocumentEmbedding)
            .filter(DocumentEmbedding.chunk_id == chunk_id)
            .first()
        )
