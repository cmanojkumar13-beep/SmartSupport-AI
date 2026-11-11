
import chromadb
from src.embeddings import generate_embeddings

# Connect to ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_db"
)

# Create or get collection
collection = client.get_or_create_collection(
    name="customer_support"
)


def store_documents(documents):
    # Generate embeddings
    embeddings = generate_embeddings(documents)

    # Generate unique IDs
    ids = [f"doc_{i}" for i in range(collection.count(),
                                       collection.count() + len(documents))]

    # Store documents and embeddings
    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

    print("Documents stored successfully!")
    print("Total documents:", collection.count())


if __name__ == "__main__":

    documents = [
        "You can reset your password using the Forgot Password option.",
        "Our customer support team is available 24 hours.",
        "You can contact support through email or phone.",
        "Our business hours are Monday to Friday, 9 AM to 6 PM."
    ]

    store_documents(documents)
