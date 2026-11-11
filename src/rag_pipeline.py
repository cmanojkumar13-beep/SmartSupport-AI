
import os
import chromadb
import time

from dotenv import load_dotenv
from google import genai
from src.embeddings import generate_embeddings

load_dotenv()

# Gemini configuration
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Gemini API key not found!")

llm_client = genai.Client(api_key=API_KEY)

# ChromaDB connection
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="customer_support"
)


# Retrieve documents
def retrieve_documents(query, top_k=2):

    if collection.count() == 0:
        return []

    query_embedding = generate_embeddings([query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=min(top_k, collection.count())
    )

    return results["documents"][0] if results["documents"] else []


# Generate response
def generate_response(question, context):

    prompt = f"""
    You are a customer support assistant.
    Answer briefly using only the context.

    Context:
    {context}

    Question:
    {question}

    If the answer is unavailable, say:
    "I don't have enough information to answer that."
    """

    response = llm_client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
        config={
            "temperature": 0.2,
            "max_output_tokens": 256
        }
    )

    return response.text or "No response generated."


# Complete RAG pipeline
def rag_pipeline(question):

    start_time = time.time()

    documents = retrieve_documents(question)

    if not documents:
        return "No relevant documents found."

    context = "\n".join(documents)

    answer = generate_response(question, context)

    elapsed = time.time() - start_time

    print(f"Response generated in {elapsed:.2f} seconds")

    return answer


if __name__ == "__main__":

    question = "How can I reset my password?"

    print("AI:", rag_pipeline(question))
