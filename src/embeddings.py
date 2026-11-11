
from sentence_transformers import SentenceTransformer

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(texts):
    embeddings = model.encode(
        texts,
        show_progress_bar=False,
        convert_to_numpy=True
    )

    return embeddings.tolist()
