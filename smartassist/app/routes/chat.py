from fastapi import APIRouter

from app.schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Day 1: simple echo. Replaced by the RAG + LLM pipeline from Day 5-6 onward.
    return ChatResponse(reply=f"You said: {request.message}")
