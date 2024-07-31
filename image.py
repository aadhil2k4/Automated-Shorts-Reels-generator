import os
import requests
from dotenv import load_dotenv
from trends import getMostTrending

load_dotenv()

def fetch_image(query):
    UNSPLASH_API = os.getenv("UNSPLASH_API")
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "client_id": UNSPLASH_API,
        "per-page": 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data['results']:
        image_url = data['results'][0]['urls']['regular']
        image_response = requests.get(image_url)

        image_path = './trending_image.jpg'
        with open(image_path, 'wb') as file:
            file.write(image_response.content)
        print(f"Image downloaded at: {image_path}")
        return image_path
    else:
        print("No images found for the trending topic.")
        return None
    
if __name__ == "__main__":
    most_trending = getMostTrending()
    fetch_image(most_trending)