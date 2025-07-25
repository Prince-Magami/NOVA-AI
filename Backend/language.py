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
