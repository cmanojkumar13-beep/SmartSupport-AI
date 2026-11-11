
import json

from src.rag_pipeline import generate_answer

with open(
    "evaluation/test_questions.json",
    "r",
    encoding="utf-8"
) as file:
    questions = json.load(file)

for item in questions:

    result = generate_answer(item["question"])

    print("\nQuestion:", item["question"])
    print("Expected topic:", item["expected_topic"])
    print("AI Answer:", result["answer"])
    print("Sources:", result["sources"])
    print("-" * 60)
