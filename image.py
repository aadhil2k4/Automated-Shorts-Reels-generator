import asyncio
from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv
import os

load_dotenv()

async def fetch_image(query):
    path = './trending_img.jpg'
    gis = GoogleImagesSearch(os.getenv('GCS_KEY'), os.getenv('GCS_CX'))
    search_params = {
        'q': query,
        'num': 1,
        'fileType': 'jpg|png',
        'safe': 'medium',
        'imgType': 'photo',
        'imgSize': 'medium'
    }
    gis.search(search_params=search_params, path_to_dir='./', custom_image_name='trending_img')
    return path