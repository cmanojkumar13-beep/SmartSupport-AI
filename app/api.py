
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.rag_pipeline import generate_answer

app = FastAPI(
    title="SmartSupport AI API",
    description="RAG-based Customer Support API",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "SmartSupport AI API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    try:
        result = generate_answer(request.question)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
