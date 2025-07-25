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


# backend/routes/finance.py
from fastapi import APIRouter, Request
from utils.helpers import generate_budget_plan, suggest_careers
from utils.audio import voice_to_text

router = APIRouter()

@router.post("/api/finance/budget")
async def budget_planner(req: Request):
    data = await req.json()
    budget_info = data.get("budget")
    response = await generate_budget_plan(budget_info)
    return {"plan": response}

@router.post("/api/finance/career")
async def career_advisor(req: Request):
    data = await req.json()
    interests = data.get("interests")
    career = await suggest_careers(interests)
    return {"career": career}


# backend/routes/health.py
from fastapi import APIRouter, Request
from utils.helpers import analyze_symptoms, translate_medical_text
from utils.audio import voice_to_text

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


# backend/routes/education.py
from fastapi import APIRouter, Request
from utils.helpers import fetch_summary, generate_quiz, scan_link_with_virustotal

router = APIRouter()

@router.post("/api/edu/summary")
async def summary(req: Request):
    data = await req.json()
    topic = data.get("topic")
    result = await fetch_summary(topic)
    return {"summary": result}

@router.post("/api/edu/quiz")
async def quiz(req: Request):
    data = await req.json()
    topic = data.get("topic")
    result = await generate_quiz(topic)
    return {"quiz": result}

@router.post("/api/edu/scan")
async def scan(req: Request):
    data = await req.json()
    url_or_email = data.get("input")
    result = await scan_link_with_virustotal(url_or_email)
    return {"report": result}


# backend/routes/language.py
from fastapi import APIRouter, Request

router = APIRouter()

LANGUAGES = ["English", "Pidgin", "Hausa", "Igbo", "Yoruba"]

@router.get("/api/langs")
def get_languages():
    return {"languages": LANGUAGES}

@router.post("/api/setlang")
async def set_language(req: Request):
    data = await req.json()
    lang = data.get("lang")
    if lang in LANGUAGES:
        return {"status": "Language set", "lang": lang}
    return {"error": "Unsupported language"}
