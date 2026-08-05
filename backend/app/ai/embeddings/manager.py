from sentence_transformers import SentenceTransformer


class EmbeddingManager:

    def __init__(self):

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(
        self,
        text: str,
    ) -> list[float]:

        vector = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return vector.tolist()

    def embed_many(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        vectors = self.model.encode(
            texts,
            normalize_embeddings=True,
        )

        return vectors.tolist()
