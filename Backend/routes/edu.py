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
