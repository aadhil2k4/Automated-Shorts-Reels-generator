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
            f"The script should explain a unique, verifiable fact or story. Ensure the information is accurate and provide the source of the fact or story.")
    #print(response['generated_text'])
    return response.text

if __name__ == "__main__":
    generate_question()
