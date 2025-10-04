import streamlit as st
import os
from video_search_tool import video_search_tool
from transcription_tool import transcription_tool
from knowledge_base import save_transcript

# Ensure folder exists
os.makedirs("knowledge_base", exist_ok=True)

st.set_page_config(page_title="AI Video Agent", layout="centered")
st.title("🤖 AI Video Agent")
st.write("Ask anything — I'll find a YouTube video and transcribe it!")

# Input + Button
query = st.text_input("❓ Your question:", placeholder="e.g., What is photosynthesis?")
run = st.button("🔍 Get Transcript")

# Ambiguous terms mapping
ambiguous_terms = {
    "python": "python programming language",
    "java": "Java programming language",
    "gravity": "gravity physics",
    "mercury": "mercury element",
    "apple": "Apple Inc. technology",
    "tesla": "Tesla electric cars",
}

# Only run when button is clicked AND query is not empty
if run:
    if not query.strip():
        st.warning("⚠️ Please enter a question.")
    else:
        try:
            enhanced_query = ambiguous_terms.get(query.lower().strip(), query)
            
            with st.spinner(f"🔍 Searching YouTube for: '{enhanced_query}'..."):
                video_url = video_search_tool(enhanced_query)
            
            st.video(video_url)  # Show video
            
            with st.spinner("🎙️ Transcribing video..."):
                transcript = transcription_tool(video_url)
            
            # Save (optional in cloud, but safe)
            save_transcript(query, video_url, transcript)
            
            st.success("✅ Done!")
            st.subheader("📝 Transcript")
            st.text_area("Full transcript:", transcript, height=300)
            
            st.download_button(
                "📥 Download Transcript",
                transcript,
                file_name=f"{query[:20].replace(' ', '_')}_transcript.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"💥 Error: {str(e)}")
            st.info("💡 Tip: Try a more specific query like 'photosynthesis for kids'.")