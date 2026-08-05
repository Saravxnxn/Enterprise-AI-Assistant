from pathlib import Path

import faiss
import numpy as np


class VectorStoreManager:

    INDEX_PATH = Path("storage/faiss/document.index")

    DIMENSION = 384

    def __init__(self):

        self.INDEX_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if self.INDEX_PATH.exists():

            self.index = faiss.read_index(str(self.INDEX_PATH))

        else:

            self.index = faiss.IndexFlatIP(self.DIMENSION)

    def add_vectors(
        self,
        vectors: list[list[float]],
    ):

        array = np.array(
            vectors,
            dtype=np.float32,
        )

        self.index.add(array)

        faiss.write_index(
            self.index,
            str(self.INDEX_PATH),
        )

    def search(
        self,
        vector: list[float],
        top_k: int = 5,
    ):

        query = np.array(
            [vector],
            dtype=np.float32,
        )

        distances, indices = self.index.search(
            query,
            top_k,
        )

        return distances, indices
