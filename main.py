from trends import getMostTrending
from image import fetch_image
from question import generate_question

if __name__ == "__main__":

    most_trending = getMostTrending()
    script = generate_question()
    image_path = fetch_image(most_trending)

    print(f"Script: {script}")
    print(f"Image Path: {image_path}")
