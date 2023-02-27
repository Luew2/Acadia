import openai
import requests
import uuid
import os
from generators.types.typeGenerator import randomSticker


# Convert size to correct format
def size_converter(size) -> str:
    """Converts size to correct format for OpenAI API"""
    if size == "256":
        return "256x256"
    elif size == "512":
        return "512x512"
    elif size == "1024":
        return "1024x1024"
    else:
        print(
            "Defaulting to size 256x256, specify size with -size 256, -size 512, or -size 1024"
        )
        return "256x256"


def number_converter(number) -> int:
    """Converts number to correct format for OpenAI API"""
    if number == None:
        return 1
    else:
        return number


# Create image
def generate_dalle(size="", number=1) -> None:
    """Generates a sticker with the DALL-E model"""
    number = number_converter(number)
    for number in range(number):
        sticker = randomSticker()
        response = openai.Image.create(prompt=sticker, n=1, size=size_converter(size))

        imageUrl = response["data"][0]["url"]
        imgData = requests.get(imageUrl).content

        randName = str(uuid.uuid4()) + ".png"

        path = "../Sticker_Generator/data/"
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)

        with open("../Sticker_Generator/data/" + randName, "wb") as handler:
            handler.write(imgData)
    print("Sticker(s) generated in Acadia/Sticker_Generator/data")
