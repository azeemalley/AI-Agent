import os
import requests

# Detect if we're running in Streamlit Cloud
IN_STREAMLIT_CLOUD = False

try:
    import streamlit as st
    # Check if we're in Streamlit Cloud by looking for environment variable
    if "STREAMLIT_CLOUD" in os.environ or "STREAMLIT_SERVER" in os.environ:
        IN_STREAMLIT_CLOUD = True
except ImportError:
    pass

def get_serpapi_key():
    """Get SerpApi key from .env (local) or st.secrets (cloud)."""
    if IN_STREAMLIT_CLOUD:
        try:
            return st.secrets["SERPAPI_API_KEY"]
        except KeyError:
            raise ValueError("❌ SERPAPI_API_KEY not found in Streamlit Secrets!")
    else:
        # Local mode: use .env
        try:
            from dotenv import load_dotenv
            load_dotenv()
            key = os.getenv("SERPAPI_API_KEY")
            if key:
                return key
            else:
                raise ValueError("❌ SERPAPI_API_KEY not found in .env file!")
        except ImportError:
            raise ValueError("❌ python-dotenv not installed. Run 'pip install python-dotenv'")

def video_search_tool(query: str) -> str:
    api_key = get_serpapi_key()
    params = {
        "engine": "youtube",
        "search_query": query,
        "api_key": api_key,
        "num": 1,
        "sp": "EgIwAQ%3D%3D"
    }

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    if "video_results" in data and len(data["video_results"]) > 0:
        video_url = data["video_results"][0]["link"]
        print(f"✅ Found video: {video_url}")
        return video_url
    else:
        raise Exception("❌ No relevant video found.")