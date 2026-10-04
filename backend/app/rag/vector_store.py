from sentence_transformers import SentenceTransformer

import faiss

import numpy as np

import os

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

VECTOR_DB_DIR = "vector_db"
os.makedirs(VECTOR_DB_DIR, exist_ok=True)

INDEX_PATH = os.path.join(
    VECTOR_DB_DIR,
    "faiss.index"
)

CHUNKS_PATH = os.path.join(
    VECTOR_DB_DIR,
    "chunks.npy"
)


def create_embeddings(chunks):

    embeddings = model.encode(chunks)

    return np.array(
        embeddings
    ).astype("float32")


def save_index(chunks):

    embeddings = create_embeddings(chunks)

    # existing database
    if os.path.exists(INDEX_PATH):

        index = faiss.read_index(
            INDEX_PATH
        )

        old_chunks = np.load(
            CHUNKS_PATH,
            allow_pickle=True
        ).tolist()

    # new database
    else:

        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(
            dimension
        )

        old_chunks = []

    # add new embeddings
    index.add(embeddings)

    # append chunks
    all_chunks = old_chunks + chunks

    # save
    faiss.write_index(
        index,
        INDEX_PATH
    )

    np.save(
        CHUNKS_PATH,
        np.array(all_chunks, dtype=object)
    )


def load_index():

    if not os.path.exists(INDEX_PATH):

        return None, None

    index = faiss.read_index(INDEX_PATH)

    chunks = np.load(
        CHUNKS_PATH,
        allow_pickle=True
    )

    return index, chunks


def search(query, k=3):

    index, chunks = load_index()

    if index is None:

        return []

    query_embedding = model.encode(
        [query]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        k
    )

    retrieved_chunks = [
        chunks[i]
        for i in indices[0]
    ]

    return retrieved_chunks

def clear_index():

    if os.path.exists(INDEX_PATH):
        os.remove(INDEX_PATH)

    if os.path.exists(CHUNKS_PATH):
        os.remove(CHUNKS_PATH)
