from fastapi import APIRouter, HTTPException
from app.services.llm_service import generate_summary

router = APIRouter()

@router.post("/summarize")
def summarize(data: dict):
    """
    Summarize the given text using LLM.
    """
    input_text = data.get("text", "")
    if not input_text:
        raise HTTPException(status_code=400, detail="Input text is required.")
    summary = generate_summary(input_text)
    return {"summary": summary}
