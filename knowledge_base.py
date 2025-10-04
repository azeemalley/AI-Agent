import os
from datetime import datetime

def save_transcript(query: str, video_url: str, transcript: str):
    os.makedirs("knowledge_base", exist_ok=True)
    
    safe_name = "".join(c if c.isalnum() else "_" for c in query[:30])
    filename = f"knowledge_base/{safe_name}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Question: {query}\n")
        f.write(f"Video: {video_url}\n")
        f.write("\n" + "="*50 + "\n\n")
        f.write(transcript)
    
    print(f"📁 Saved transcript to: {filename}")
    return filename