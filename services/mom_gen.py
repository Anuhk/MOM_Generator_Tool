#LLM Logic

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config={
        "temperature": 0.2,
        "top_p": 0.9
    }
)



def generate_mom(transcript):
    prompt = f"""
You are a professional meeting assistant.

Create structured Minutes of Meeting (MoM) from the transcript below.

Include:
1. Agenda (infer if needed)
2. Key discussion points
3. Decisions made
4. Action items (Task | Owner | Deadline)
5. Risks or blockers

Rules:
- Be concise
- Do NOT invent information
- If owner or deadline not mentioned, write "Not specified"

Transcript:
{transcript}
"""

    response = model.generate_content(prompt)
    return response.text
