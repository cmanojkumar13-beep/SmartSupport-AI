
import os
import chromadb

from src.embeddings import generate_embeddings

# Project paths
DATA_FILE = os.path.join("data", "customer_support.txt")
DB_PATH = "./chroma_db"

# Connect to ChromaDB
client = chromadb.PersistentClient(path=DB_PATH)

# Get or create collection
collection = client.get_or_create_collection(
    name="customer_support"
)


def load_documents(file_path):
    """Read and split the knowledge-base document."""

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Document not found: {file_path}"
        )

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Split text into manageable chunks
    chunks = [
        chunk.strip()
        for chunk in text.split("\n\n")
        if chunk.strip()
    ]

    return chunks


def ingest_documents():
    """Generate embeddings and store documents."""

    documents = load_documents(DATA_FILE)

    if not documents:
        print("No documents found!")
        return

    # Generate embeddings
    embeddings = generate_embeddings(documents)

    # Generate unique IDs
    ids = [
        f"customer_support_{i}"
        for i in range(len(documents))
    ]

    # Upsert prevents duplicate IDs on repeated runs
    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

    print("\nIngestion completed successfully!")
    print("Documents processed:", len(documents))
    print("Total ChromaDB records:", collection.count())


if __name__ == "__main__":
    ingest_documents()
