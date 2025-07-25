# backend/routes/finance.py
from fastapi import APIRouter, Request
from backend.utils.helpers import generate_budget_plan, suggest_careers
from backend.utils.audio import voice_to_text

router = APIRouter()

@router.post("/api/finance/budget")
async def plan_budget(req: Request):
    body = await req.json()
    budget = body.get("budget") or ""
    voice = body.get("voice")
    
    if voice:
        budget = voice_to_text(voice)
    
    result = generate_budget_plan(budget)
    return {"plan": result}

@router.post("/api/finance/career")
async def match_career(req: Request):
    body = await req.json()
    interests = body.get("interests", "")
    return {"career": suggest_careers(interests)}


# backend/routes/health.py
from fastapi import APIRouter, Request
from backend.utils.helpers import analyze_symptoms, translate_text
from backend.utils.audio import voice_to_text

router = APIRouter()

@router.post("/api/health/symptoms")
async def check_symptoms(req: Request):
    body = await req.json()
    symptoms = body.get("symptoms", "")
    return {"result": analyze_symptoms(symptoms)}

@router.post("/api/health/translate")
async def medical_translate(req: Request):
    body = await req.json()
    text = body.get("text")
    voice = body.get("voice")
    lang = body.get("lang", "en")

    if voice:
        text = voice_to_text(voice)
    
    return {"translated": translate_text(text, lang)}


# backend/routes/education.py
from fastapi import APIRouter, Request
from backend.utils.helpers import get_topic_summary, generate_quiz, scan_link_or_email

router = APIRouter()

@router.post("/api/edu/summary")
async def topic_summary(req: Request):
    body = await req.json()
    topic = body.get("topic", "")
    return {"summary": get_topic_summary(topic)}

@router.post("/api/edu/quiz")
async def quiz_creator(req: Request):
    body = await req.json()
    topic = body.get("topic", "")
    return {"quiz": generate_quiz(topic)}

@router.post("/api/edu/scan")
async def email_or_link_scan(req: Request):
    body = await req.json()
    data = body.get("data", "")
    return scan_link_or_email(data)


# backend/routes/language.py
from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/api/language")
async def set_language(req: Request):
    body = await req.json()
    selected = body.get("lang", "en")
    return {"selected": selected, "status": "Language mode updated"}
