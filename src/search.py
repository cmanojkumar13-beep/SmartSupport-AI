
import chromadb
from src.embeddings import generate_embeddings

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="customer_support"
)


def search_documents(query):

    query_embedding = generate_embeddings([query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=2
    )

    print("\nUser Query:", query)
    print("\nRelevant Documents:")

    for document in results["documents"][0]:
        print("-", document)


if __name__ == "__main__":
    search_documents("How do I change my password?")
