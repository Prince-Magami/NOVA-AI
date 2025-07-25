# backend/app.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from routes import chat, finance, health, education, language

load_dotenv()

app = FastAPI()

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routes
app.include_router(chat.router, prefix="/api/chat")
app.include_router(finance.router, prefix="/api/finance")
app.include_router(health.router, prefix="/api/health")
app.include_router(education.router, prefix="/api/edu")
app.include_router(language.router, prefix="/api/lang")

@app.get("/")
def read_root():
    return {"status": "🚀 NOVA AI Backend is Running!"}
