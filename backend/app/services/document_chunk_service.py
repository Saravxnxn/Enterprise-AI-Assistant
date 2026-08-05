from app.ai.chunking.manager import ChunkManager
from app.models.document_chunk import DocumentChunk
from app.repositories.document_chunk_repository import (
    DocumentChunkRepository,
)


class DocumentChunkService:

    def __init__(
        self,
        repository: DocumentChunkRepository,
    ):
        self.repository = repository
        self.chunk_manager = ChunkManager()

    def create_chunks(
        self,
        document_id: int,
        content: str,
    ):

        chunks = self.chunk_manager.split(content)

        models = []

        for index, chunk in enumerate(chunks):

            models.append(
                DocumentChunk(
                    document_id=document_id,
                    chunk_index=index,
                    content=chunk,
                )
            )

        return self.repository.create_many(models)
