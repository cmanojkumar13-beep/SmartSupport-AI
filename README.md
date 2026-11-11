
# SmartSupport AI – Customer Support Assistant

## Project Overview
SmartSupport AI is an AI-powered customer support assistant
that uses Retrieval-Augmented Generation (RAG) to answer
customer questions using a knowledge base.

## Features
- AI-powered customer support
- Document ingestion
- Text embeddings
- ChromaDB vector database
- Semantic document retrieval
- LLM-based answer generation
- Streamlit chat interface
- Chat history

## Technologies Used
- Python
- Streamlit
- ChromaDB
- Embeddings
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)

## Project Structure
- app.py – Streamlit application
- ingest.py – Document ingestion
- src/embeddings.py – Embedding generation
- src/vector_store.py – Vector database
- src/rag_pipeline.py – RAG pipeline
- data/ – Sample knowledge base

## Installation

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Configure your required API key.
5. Ingest documents.

```bash
python ingest.py
```

6. Run the application.

```bash
python -m streamlit run app.py
```

## Application
SmartSupport AI provides answers based on
information available in its knowledge base.

## Author
Manoj Kumar
