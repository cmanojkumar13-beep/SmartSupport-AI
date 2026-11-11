
import sys
import os

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from src.vector_store import load_vector_store

def get_retriever():
    vector_store = load_vector_store()
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )
    return retriever
