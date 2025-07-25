from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Explicit module imports
from routes.chat import router as chat_router
from routes.finance import router as finance_router
from routes.health import router as health_router
from routes.education import router as education_router
from routes.language import router as language_router

app = FastAPI()

# CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(chat_router, prefix="/chat", tags=["Chat"])
app.include_router(finance_router, prefix="/finance", tags=["Finance"])
app.include_router(health_router, prefix="/health", tags=["Health"])
app.include_router(education_router, prefix="/education", tags=["Education"])
app.include_router(language_router, prefix="/language", tags=["Language"])

@app.get("/")
def home():
    return {"message": "🌍 Nova AI Backend is alive"}
