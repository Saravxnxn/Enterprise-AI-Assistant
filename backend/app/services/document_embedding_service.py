import json

from app.ai.embeddings.manager import EmbeddingManager
from app.models.document_embedding import DocumentEmbedding
from app.repositories.document_embedding_repository import (
    DocumentEmbeddingRepository,
)


class DocumentEmbeddingService:

    MODEL_NAME = "all-MiniLM-L6-v2"

    def __init__(
        self,
        repository: DocumentEmbeddingRepository,
    ):

        self.repository = repository

        self.embedding_manager = EmbeddingManager()

    def create_embeddings(
        self,
        chunks,
    ):

        texts = [chunk.content for chunk in chunks]

        vectors = self.embedding_manager.embed_many(texts)

        models = []

        for chunk, vector in zip(
            chunks,
            vectors,
            strict=False,
        ):

            models.append(
                DocumentEmbedding(
                    chunk_id=chunk.id,
                    embedding=json.dumps(vector),
                    model_name=self.MODEL_NAME,
                )
            )

        return self.repository.create_many(models)
