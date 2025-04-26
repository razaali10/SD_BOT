
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/parse")
async def parse_text(input_data: TextInput):
    try:
        prompt = f"""
Extract causal relationships from the following paragraph.
Format each link like: [Cause Variable] → [Effect Variable] (+/-)

Rules:
- (+) if Cause increases Effect
- (-) if Cause decreases Effect
- Only output the causal links, one per line.
- No explanations, no introductions.

Paragraph:
{input_data.text}
"""

        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=500
        )

        output_text = response['choices'][0]['message']['content']
        lines = output_text.strip().split("\n")

        causal_links = []
        for line in lines:
            line = line.strip()
            if "→" in line and ("(+)" in line or "(-)" in line):
                causal_links.append(line)

        return {
            "causal_relationships": causal_links
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
