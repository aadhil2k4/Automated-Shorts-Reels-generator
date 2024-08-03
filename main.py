import asyncio
from trends import getMostTrending
from image import fetch_image
from question import generate_question
from movie import create_clip

async def main():
    most_trending = getMostTrending()
    image_path = await fetch_image(most_trending)
    script = await generate_question()
    create_clip(image_path, script)

if __name__ == "__main__":
    asyncio.run(main())