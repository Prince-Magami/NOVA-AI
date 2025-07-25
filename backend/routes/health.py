# backend/routes/health.py
from fastapi import APIRouter, Request
from utils.helpers import analyze_symptoms, translate_medical_text
#from utils.audio import voice_to_text

router = APIRouter()

@router.post("/api/health/symptoms")
async def health_symptoms(req: Request):
    data = await req.json()
    text = data.get("symptoms")
    result = await analyze_symptoms(text)
    return {"result": result}

@router.post("/api/health/translate")
async def health_translate(req: Request):
    data = await req.json()
    text = data.get("text")
    translated = await translate_medical_text(text)
    return {"translated": translated}

