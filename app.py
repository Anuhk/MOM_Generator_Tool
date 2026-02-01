#UI 

from dotenv import load_dotenv
from utils.text_util import clean_transcript
load_dotenv()  

import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


import streamlit as st
from services.audio import extract_audio
from services.transcribe import transcribe
from services.mom_gen import generate_mom



st.title("AI MoM Generator")

uploaded_file = st.file_uploader(
    "Upload meeting recording",
    type=["mp4", "wav", "mp3"]
)


if uploaded_file:
    os.makedirs("temp", exist_ok=True)
    file_path = f"temp/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded successfully")

    
    audio_path = extract_audio(file_path)
    st.success("Audio extracted")


    with st.spinner("Transcribing audio..."):
        transcript = transcribe(audio_path)

    st.text_area("Transcript", transcript, height=200)


    cleaned = clean_transcript(transcript)

    with st.spinner("Generating MoM..."):
        mom = generate_mom(cleaned)

    st.subheader("Minutes of Meeting")
    st.text_area("MoM", mom, height=400)
