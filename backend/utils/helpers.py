import os
import requests
from dotenv import load_dotenv

# 🔐 Load environment variables
load_dotenv()

# 🔐 API Keys
gemini_api = os.getenv("GEMINI_API")
virustotal_api = os.getenv("VT_API")
career_api = os.getenv("CAREER_API")
translator_api = os.getenv("TRANSLATOR_API")
health_api = os.getenv("HEALTH_API")


# 🌐 Generic Gemini API Wrapper
def call_gemini_api(prompt):
    try:
        res = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {gemini_api}",
                "Content-Type": "application/json"
            },
            json={
                "model": "google/gemini-pro",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[Gemini Error] {str(e)}"


# 📊 Budget Planner
def generate_budget_plan(budget):
    prompt = f"You're a financial assistant. Help plan this budget: {budget}"
    return call_gemini_api(prompt)


# 🧠 Career Suggestion
def suggest_careers(interests):
    prompt = f"Suggest realistic job paths for someone interested in: {interests}"
    return call_gemini_api(prompt)


# 🧬 Symptom Analysis
def analyze_symptoms(symptoms):
    prompt = f"Act like a smart health bot. Suggest possible conditions based on: {symptoms}"
    return call_gemini_api(prompt)


# 🌍 Translate Medical Text
def translate_medical_text(text, lang="en"):
    prompt = f"Translate this medical text into {lang}: {text}"
    return call_gemini_api(prompt)


# 📚 Educational Summary
def generate_summary(topic):
    prompt = f"Summarize the topic: {topic} in simple words for students."
    return call_gemini_api(prompt)


# 📝 Quiz Generator
def generate_quiz(topic):
    prompt = f"Generate 3 quiz questions based on the topic: {topic}. Include answers."
    return call_gemini_api(prompt)


# 🛡️ VirusTotal Link/Email Scanner
def scan_virustotal(input_data):
    try:
        url = "https://www.virustotal.com/api/v3/urls"
        encoded = requests.post(
            url,
            headers={"x-apikey": virustotal_api},
            data={"url": input_data}
        ).json()

        scan_id = encoded.get("data", {}).get("id", None)
        if not scan_id:
            return "Invalid input. Couldn’t scan."

        result = requests.get(
            f"https://www.virustotal.com/api/v3/analyses/{scan_id}",
            headers={"x-apikey": virustotal_api}
        )
        analysis = result.json().get("data", {}).get("attributes", {})
        stats = analysis.get("stats", {})

        summary = (
            f"Malicious: {stats.get('malicious', 0)}, "
            f"Suspicious: {stats.get('suspicious', 0)}, "
            f"Harmless: {stats.get('harmless', 0)}"
        )
        return summary

    except Exception as e:
        return f"[VT Error] {str(e)}"


# 🌐 Language Code Mapper
def map_language_code(lang):
    return {
        "English": "en",
        "Nigerian Pidgin": "pcm",
        "Hausa": "ha",
        "Igbo": "ig",
        "Yoruba": "yo"
    }.get(lang, "en")


# Aliases for external use
fetch_summary = generate_summary
scan_link_with_virustotal = scan_virustotal

ask_gemini = call_gemini_api
