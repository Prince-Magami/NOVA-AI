from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.chat import router as chat_router
from routes.edu import router as edu_router
from routes.finance import router as finance_router
from routes.health import router as health_router
from routes.language import router as language_router
from utils.helpers import ask_gemini, generate_summary


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
def root():
    return {"message": "NOVA API is live"}

@app.post("/")
async def handle_post(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    
    # You can import and call your AI function here, e.g.:
    from utils.helpers import call_gemini_api
    try:
        response = call_gemini_api(prompt)
        return {"response": response}
    except Exception as e:
        return {"response": f"[ERROR] {str(e)}"}
