# backend/routes/chat.py
from fastapi import APIRouter, Request
from utils.helpers import call_gemini_api

router = APIRouter()

@router.post("/api/chat")
async def chat_with_nova(req: Request):
    data = await req.json()
    user_message = data.get("message")

    if not user_message:
        return {"reply": "Please enter a message."}

    reply = await call_gemini_api(user_message)
    return {"reply": reply}
