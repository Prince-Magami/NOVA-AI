# app.py
import os
import cohere
import httpx
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Allow all CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class ChatRequest(BaseModel):
    message: str
    mode: str  # 'chat', 'health', 'education', 'finance'
    lang: str  # 'en', 'fr', 'ha', etc.

# Load API Keys
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize Cohere Client
co = cohere.Client(COHERE_API_KEY)

# 🌐 Main Chat Endpoint
@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    system_prompts = {
        "chat": "You are a creative, fun, futuristic AI assistant who chats freely with users.",
        "health": "You are a medical AI assistant. Help users identify symptoms, translate prescriptions, and offer health advice. Be careful not to diagnose.",
        "education": "You are an educational AI assistant helping students with explanations, summaries, and study tips.",
        "finance": "You are a business/finance AI advisor giving tips for managing money, starting businesses, and discovering talents."
    }

    prompt = f"{system_prompts.get(req.mode, system_prompts['chat'])}\nLanguage: {req.lang}\nUser: {req.message}"

    response = co.chat(message=prompt, model="command-r-plus", temperature=0.8)

    return {"reply": response.text}


# 🧪 Email/Link Scam Scanner (Future expansion)
@app.post("/scan")
async def scan_link(request: Request):
    data = await request.json()
    url = data.get("url")

    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    api_url = f"https://www.virustotal.com/api/v3/urls"

    try:
        async with httpx.AsyncClient() as client:
            encoded_url = httpx.QueryParams({'url': url})
            response = await client.post(api_url, data=encoded_url, headers=headers)
            url_id = response.json()["data"]["id"]

            result = await client.get(f"https://www.virustotal.com/api/v3/analyses/{url_id}", headers=headers)
            analysis = result.json()

        stats = analysis["data"]["attributes"]["stats"]
        return {"harmless": stats["harmless"], "malicious": stats["malicious"], "suspicious": stats["suspicious"]}
    except Exception as e:
        return {"error": str(e)}


# 🔁 Test Root
@app.get("/")
def root():
    return {"message": "NOVA AI Backend is live!"}
