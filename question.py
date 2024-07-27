import os
import google.generativeai as genai
from trends import getMostTrending
from dotenv import load_dotenv

load_dotenv()

most_trending = getMostTrending()

genai.configure(api_key=os.getenv('GEMINI_KEY'))

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content(f"Generate a multiple-choice question about {most_trending} based on a well-established and verifiable fact. "
          f"Provide 4 answer options where only one option is correct and clearly distinct from the incorrect options. "
          f"At the end, mention the correct answer and provide a brief explanation supporting it.")
print(response.text)
