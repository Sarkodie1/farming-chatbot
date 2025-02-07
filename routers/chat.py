from fastapi import APIRouter, HTTPException
from models.chat import ChatRequest, ChatResponse
from services.groq_service import GroqService

router = APIRouter()
groq_service = GroqService()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        reply = groq_service.get_chat_completion(request.message)
        return ChatResponse(user_message=request.message, bot_reply=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
