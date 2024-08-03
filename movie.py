import os
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip, TextClip
from gtts import gTTS
from image import fetch_image
from question import generate_question
from trends import getMostTrending
from dotenv import load_dotenv

load_dotenv()

def generate_audio(text, filename="narration.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    return filename

def create_clip(image_path, text, output_path="short.mp4"):
    audio_path = generate_audio(text)
    image_clip = ImageClip(image_path)
    audio_clip = AudioFileClip(audio_path)
    image_clip = image_clip.set_duration(audio_clip.duration)
    video = image_clip.set_audio(audio_clip)
    video.write_videofile(output_path, fps=24)
