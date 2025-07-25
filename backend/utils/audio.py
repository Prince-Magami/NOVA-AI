# backend/utils/audio.py

import speech_recognition as sr
import pyttsx3
import tempfile
from pydub import AudioSegment

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# 🔊 Convert Speech (audio file) to Text
def speech_to_text(audio_file):
    try:
        with tempfile.NamedTemporaryFile(delete=True, suffix=".wav") as temp_wav:
            audio = AudioSegment.from_file(audio_file)
            audio.export(temp_wav.name, format="wav")
            with sr.AudioFile(temp_wav.name) as source:
                audio_data = recognizer.record(source)
                return recognizer.recognize_google(audio_data)
    except Exception as e:
        return f"Error processing audio: {str(e)}"

# 🗣️ Convert Text to Speech and return audio bytes
def text_to_speech(text):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_mp3:
            tts_engine.save_to_file(text, temp_mp3.name)
            tts_engine.runAndWait()
            with open(temp_mp3.name, "rb") as f:
                audio_bytes = f.read()
            return audio_bytes
    except Exception as e:
        return None
