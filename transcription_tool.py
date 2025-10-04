import os
import google.generativeai as genai

# Detect if we're running in Streamlit Cloud
IN_STREAMLIT_CLOUD = False

try:
    import streamlit as st
    # Check if we're in Streamlit Cloud by looking for environment variable
    if "STREAMLIT_CLOUD" in os.environ or "STREAMLIT_SERVER" in os.environ:
        IN_STREAMLIT_CLOUD = True
except ImportError:
    pass

def get_gemini_key():
    """Get Gemini key from .env (local) or st.secrets (cloud)."""
    if IN_STREAMLIT_CLOUD:
        try:
            return st.secrets["GEMINI_API_KEY"]
        except KeyError:
            raise ValueError("❌ GEMINI_API_KEY not found in Streamlit Secrets!")
    else:
        # Local mode: use .env
        try:
            from dotenv import load_dotenv
            load_dotenv()
            key = os.getenv("GEMINI_API_KEY")
            if key:
                return key
            else:
                raise ValueError("❌ GEMINI_API_KEY not found in .env file!")
        except ImportError:
            raise ValueError("❌ python-dotenv not installed. Run 'pip install python-dotenv'")

def transcription_tool(video_url: str) -> str:
    api_key = get_gemini_key()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-2.5-flash')

    print("⏳ Asking Gemini to transcribe the video...")
    response = model.generate_content([
        "Transcribe the spoken words in this video accurately.",
        video_url
    ])
    return response.text