import os
import httpx
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import cohere

load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load API keys
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

# Init Cohere
co = cohere.Client(COHERE_API_KEY)


# 📩 Request Schema
class Message(BaseModel):
    user_input: str
    mode: str  # Options: "education", "medical", "finance", "chat"


# 🤖 Main Chat Endpoint
@app.post("/ask")
async def ask(msg: Message):
    prompt = build_prompt(msg.user_input, msg.mode)

    response = co.generate(
        model="command-r",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )
    return {"response": response.generations[0].text.strip()}


def build_prompt(user_input, mode):
    if mode == "education":
        return f"As an educational advisor, assist this Nigerian student with advice or study help: {user_input}"
    elif mode == "medical":
        return f"You're a health assistant. Give friendly wellness tips or possible advice (no diagnosis): {user_input}"
    elif mode == "finance":
        return f"You're a smart business mentor in Nigeria. Give simple advice to help this user: {user_input}"
    else:
        return f"You're a funny, chill Nigerian AI chatbox. Respond casually: {user_input}"


# 🔍 Link/Email Scanner
@app.post("/scan")
async def scan_link(request: Request):
    data = await request.json()
    url_to_check = data.get("url")

    headers = {
        "x-apikey": VIRUSTOTAL_API_KEY
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://www.virustotal.com/api/v3/urls", params={"url": url_to_check}, headers=headers)
            if response.status_code == 200:
                return {"result": "No known threats detected for this link."}
            else:
                return {"result": "Unable to verify this link right now."}
    except Exception as e:
        return {"result": f"Error scanning link: {str(e)}"}
