import json
from pathlib import Path

import faiss
import numpy as np


class VectorStoreManager:

    INDEX_PATH = Path("storage/faiss/document.index")

    MAPPING_PATH = Path("storage/faiss/mapping.json")

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

        if self.MAPPING_PATH.exists():

            with open(
                self.MAPPING_PATH,
                encoding="utf-8",
            ) as file:

                self.mapping = json.load(file)

        else:

            self.mapping = {}

    def add_vectors(
        self,
        vectors: list[list[float]],
        chunk_ids,
    ):

        array = np.array(
            vectors,
            dtype=np.float32,
        )

        start = self.index.ntotal

        self.index.add(array)

        for i, chunk_id in enumerate(chunk_ids):

            self.mapping[str(start + i)] = chunk_id

        with open(
            self.MAPPING_PATH,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                self.mapping,
                file,
                indent=4,
            )

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


def get_chunk_ids(
    self,
    indices,
):

    chunk_ids = []

    for index in indices:

        if index == -1:
            continue

        chunk_id = self.mapping.get(str(index))

        if chunk_id is not None:

            chunk_ids.append(chunk_id)

    return chunk_ids
