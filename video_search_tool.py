import os
import requests

def get_serpapi_key():
    """Get SerpApi key from environment (local) or Streamlit secrets (cloud)."""
    try:
        # Try Streamlit secrets (for cloud)
        import streamlit as st
        return st.secrets["SERPAPI_API_KEY"]
    except (ImportError, KeyError, AttributeError):
        # Fallback to .env (for local)
        from dotenv import load_dotenv
        load_dotenv()
        return os.getenv("SERPAPI_API_KEY")

def video_search_tool(query: str) -> str:
    api_key = get_serpapi_key()
    if not api_key:
        raise ValueError("❌ SERPAPI_API_KEY not found! Add it to .env (local) or Streamlit Secrets (cloud).")

    params = {
        "engine": "youtube",
        "search_query": query,
        "api_key": api_key,
        "num": 1,
        "sp": "EgIwAQ%3D%3D"  # Filter: video, long, not music
    }

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    if "video_results" in data and len(data["video_results"]) > 0:
        video_url = data["video_results"][0]["link"]
        print(f"✅ Found video: {video_url}")
        return video_url
    else:
        raise Exception("❌ No relevant video found.")