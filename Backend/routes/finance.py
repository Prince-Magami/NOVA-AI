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


