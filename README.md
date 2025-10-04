# 🤖 AI Video Agent: Search + Transcribe YouTube Videos

An intelligent AI agent that **searches YouTube for relevant videos** based on your question and **transcribes the audio** using Google Gemini — all in one click!

> Ask: _"What is machine learning?"_ → Get a **video + full transcript** instantly.

![AI Video Agent Demo]([https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white](https://ai-agent-7mkxjv5dsnouxvpz7qh6hb.streamlit.app/))

---

## ✨ Features

- 🔍 **Smart YouTube Search** using SerpApi (avoids music/ads)
- 🎙️ **Accurate Transcription** using **Gemini 2.5 Pro**
- 💾 **Auto-saves transcripts** to a local knowledge base
- 🌐 **Web UI** with Streamlit (works locally & online)
- 🧠 Handles ambiguous queries (e.g., `"python"` → programming, not snake)

---

## 🚀 Live Demo

Try the live web app here:  
👉 **[AI Video Agent on Streamlit Cloud]([https://your-username-ai-video-agent.streamlit.app](https://ai-agent-7mkxjv5dsnouxvpz7qh6hb.streamlit.app/))**  


---

## 🛠️ Tech Stack

- **SerpApi** – YouTube video search
- **Google Gemini API** – Video transcription (`gemini-2.5-pro`)
- **Streamlit** – Web interface
- **Python** – Core logic

---

## 📥 How to Run Locally

### Prerequisites
- Python 3.9+
- [SerpApi Account](https://serpapi.com) (free tier available)
- [Google Gemini API Key](https://aistudio.google.com/app/apikey)

### Steps

1. **Clone the repo**
   ```bash
   git clone [https://github.com/your-username/ai-video-agent.git](https://github.com/azeemalley/AI-Agent)
   cd agent
