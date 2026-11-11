
import os
import chromadb

from dotenv import load_dotenv
from google import genai
from src.embeddings import generate_embeddings

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini
client = genai.Client(api_key=API_KEY)

# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="customer_support"
)


def retrieve_documents(query):

    query_embedding = generate_embeddings([query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=2
    )

    return results["documents"][0]


def generate_answer(question):

    # Retrieve relevant documents
    documents = retrieve_documents(question)

    if not documents:
        return "No relevant information found."

    context = "\n".join(documents)

    prompt = f"""
    You are a helpful customer support AI assistant.

    Answer the user's question using only the
    following context.

    Context:
    {context}

    User Question:
    {question}

    If the answer is not available in the context,
    clearly say that you do not have enough information.

    Answer:
    """

    # Generate response
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":

    question = "How can I reset my password?"

    answer = generate_answer(question)

    print("\nUser:", question)
    print("\nAI Assistant:", answer)
