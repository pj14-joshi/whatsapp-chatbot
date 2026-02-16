# api.py
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found. Check your .env file!")

genai.configure(api_key=api_key)

# Create model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Function for chat reply
def get_gemini_reply(chat_text):
    prompt = f"""
    You are Pratham Joshi ,who is god and give short very short reply with humor
   

    Conversation:
    {chat_text}

    Write only your next reply message (no quotes, no extra text).
    """
    response = model.generate_content(prompt)
    return response.text.strip()
