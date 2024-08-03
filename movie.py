import os
from moviepy.editor import *
from gtts import gTTS
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

def generate_audio(text, filename="narration.mp3"):
    tld = 'com.au'
    tts = gTTS(text, lang='en', tld=tld)
    tts.save(filename)
    return filename

def resize_image(image_path, output_path, width, height):
    with Image.open(image_path) as img:
        img = img.resize((width, height), Image.LANCZOS)
        if img.mode == 'RGBA':
            img = img.convert('RGB')  
        img.save(output_path, format='JPEG')

def create_clip(image_path, text, output_path="short.mp4"):
    default_img_path = "default_img.jpg"
    resized_img_path = "resized_img.jpg"
    video_width, video_height = 1080, 1920

    if not image_path or not os.path.exists(image_path):
        image_path = default_img_path

    resize_image(image_path, resized_img_path, video_width, video_height)

    audio_path = generate_audio(text)
    audio_clip = AudioFileClip(audio_path)
    image_clip = ImageClip(resized_img_path)

    image_clip = image_clip.set_duration(audio_clip.duration)
    video = image_clip.set_audio(audio_clip)
    video.write_videofile(output_path, fps=24)


