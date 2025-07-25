from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.chat import router as chat_router
from backend.routes.edu import router as edu_router
from backend.routes.finance import router as finance_router
from backend.routes.health import router as health_router
from backend.routes.language import router as language_router

from backend.utils.helpers import ask_gemini, generate_summary

app = FastAPI()

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers correctly
app.include_router(chat_router, prefix="/chat", tags=["Chat"])
app.include_router(finance_router, prefix="/finance", tags=["Finance"])
app.include_router(health_router, prefix="/health", tags=["Health"])
app.include_router(edu_router, prefix="/education", tags=["Education"])
app.include_router(language_router, prefix="/language", tags=["Language"])

@app.get("/")
def home():
    return {"message": "🌍 Nova AI Backend is alive"}
