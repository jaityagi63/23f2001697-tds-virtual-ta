from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.answer_engine import generate_answer
from app.image_utils import extract_text_from_base64

import uvicorn

app = FastAPI()

class QuestionInput(BaseModel):
    question: str = ""
    image: str = None

@app.post("/api/")
async def answer_question(data: QuestionInput):
    full_question = data.question or ""

    # Extract text from image (if present)
    if data.image:
        image_text = extract_text_from_base64(data.image)
        full_question += " " + image_text

    # Generate answer
    answer, links = generate_answer(full_question)

    return {
        "answer": answer,
        "links": links
    }

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
