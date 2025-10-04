import os
import google.generativeai as genai

def get_gemini_key():
    """Get Gemini key from environment (local) or Streamlit secrets (cloud)."""
    try:
        # Try Streamlit secrets (for cloud)
        import streamlit as st
        return st.secrets["GEMINI_API_KEY"]
    except (ImportError, KeyError, AttributeError):
        # Fallback to .env (for local)
        from dotenv import load_dotenv
        load_dotenv()
        return os.getenv("GEMINI_API_KEY")

def transcription_tool(video_url: str) -> str:
    api_key = get_gemini_key()
    if not api_key:
        raise ValueError("❌ GEMINI_API_KEY not found! Add it to .env (local) or Streamlit Secrets (cloud).")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-2.5-flash')

    print("⏳ Asking Gemini to transcribe the video...")
    response = model.generate_content([
        "Transcribe the spoken words in this video accurately.",
        video_url
    ])
    return response.text