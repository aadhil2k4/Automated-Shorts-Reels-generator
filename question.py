import os
import google.generativeai as genai
from trends import getMostTrending
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def generate_question():
    most_trending = getMostTrending()

    genai.configure(api_key=os.getenv('GEMINI_KEY'))

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(f"Generate a factual and interesting YouTube Short script about {most_trending}. "
              f"The script should explain a unique, verifiable fact or story in a concise manner suitable for a 40-second video narration (fps=24)."
              f"No descriptions / symbols. The generated script converted to text using google text voiceover"
              f"No visual or Narrator should be wriiten in the generated text"
              f"No symbols like ; : # should be written in the generated text"
              f"No title should be generated")
    #print(response['generated_text'])
    return response.text

if __name__ == "__main__":
    generate_question()
