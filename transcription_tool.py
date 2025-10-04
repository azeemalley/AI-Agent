import os
import google.generativeai as genai

IN_STREAMLIT_CLOUD = False
try:
    import streamlit as st
    if "STREAMLIT_CLOUD" in os.environ:
        IN_STREAMLIT_CLOUD = True
except ImportError:
    pass

def get_gemini_key():
    if IN_STREAMLIT_CLOUD:
        return st.secrets["GEMINI_API_KEY"]
    else:
        from dotenv import load_dotenv
        load_dotenv()
        return os.getenv("GEMINI_API_KEY")

def transcription_tool(video_url: str) -> str:
    api_key = get_gemini_key()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-2.5-pro')

    # Strong prompt to prevent hallucination
    response = model.generate_content([
        "You are given a YouTube video. Transcribe ONLY the spoken words from the main audio track. "
        "Do not invent content. Do not summarize. Do not describe visuals. "
        "If the video is about machine learning, transcribe machine learning content. "
        "If the video is about history, transcribe history. But DO NOT mix topics. "
        "Return ONLY the transcript — no introductions, no conclusions.",
        video_url
    ])
    return response.text