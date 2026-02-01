AI MoM Generator

Automatically generate structured Minutes of Meeting (MoM) from recorded meetings.

Taking MoM while staying fully engaged in a meeting can be challenging. This tool provides an end-to-end solution: upload a recording, convert it to text, and generate professional MoM automatically.

Features

- Convert uploaded video/audio to mono 16kHz WAV

- Convert audio to text using Whisper

- Generate structured MoM using Gemini-2.5-flash (agenda, key points, decisions, action items, risks) [ Used google AI Studio for API key ]

- Interactive Streamlit UI for uploading recordings and viewing output

Tech Stack

- Audio Extraction: FFmpeg

- Speech-to-Text: Whisper (OpenAI)

- LLM for MoM Generation: Gemini-2.5-flash

- UI: Streamlit

- Environment Management: Python, dotenv
