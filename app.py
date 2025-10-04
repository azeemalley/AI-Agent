import streamlit as st
import os
from video_search_tool import video_search_tool
from transcription_tool import transcription_tool
from knowledge_base import save_transcript

# Ensure knowledge_base folder exists
os.makedirs("knowledge_base", exist_ok=True)

# Page config
st.set_page_config(page_title="AI Video Agent", layout="centered")
st.title("🤖 AI Video Agent")
st.write("Ask anything — I'll find a YouTube video and transcribe it for you!")

# Input box
query = st.text_input("❓ Your question:", placeholder="e.g., What is photosynthesis?")

# Ambiguous terms fix (so 'python' = programming, not snake)
ambiguous_terms = {
    "python": "python programming language",
    "java": "Java programming language",
    "gravity": "gravity physics",
    "mercury": "mercury element",
    "apple": "Apple Inc. technology",
    "tesla": "Tesla electric cars",
    "swift": "Swift programming language",
    "ruby": "Ruby programming language"
}

if st.button("🔍 Get Transcript"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        try:
            # Enhance query if it's ambiguous
            enhanced_query = ambiguous_terms.get(query.lower().strip(), query)
            
            with st.spinner(f"🔍 Searching YouTube for: '{enhanced_query}'..."):
                video_url = video_search_tool(enhanced_query)
            
            # Show video preview
            st.video(video_url)
            
            with st.spinner("🎙️ Transcribing video..."):
                transcript = transcription_tool(video_url)
            
            # Save transcript
            filename = save_transcript(query, video_url, transcript)
            
            # Show result
            st.success("✅ Transcription complete!")
            st.subheader("📝 Transcript")
            st.text_area("Full transcript:", transcript, height=300)
            
            # Download button
            st.download_button(
                "📥 Download Transcript",
                transcript,
                file_name=f"{query[:20].replace(' ', '_')}_transcript.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"💥 Error: {str(e)}")
            st.info("Tip: Try a more specific question like 'photosynthesis for kids' or 'Python for beginners'.")