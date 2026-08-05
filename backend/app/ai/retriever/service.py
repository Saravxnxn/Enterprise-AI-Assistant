from app.ai.embeddings.manager import EmbeddingManager
from app.ai.vectorstore.manager import VectorStoreManager


class RetrieverService:

    def __init__(self):

        self.embedding_manager = EmbeddingManager()

        self.vector_store = VectorStoreManager()
