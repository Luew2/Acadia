import openai
import requests
import uuid
import sys
import select
import time
import tty
import termios
import os
import cv2
import numpy as np
import random
# from generators.types.type_generator import random_sticker
# from generators.transformer.remove_background import backround_remover

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



# def loading_bar(sticker, text="Loading"):
#     generate_dalle(sticker, args.size, args.n)


#     # Clear the loading bar and display the "Sticker generated!" message
#     sys.stdout.write("\r" + " " * (len(text) + 102))
#     sys.stdout.flush()
#     sys.stdout.write("\r" + "Sticker generated!")
#     sys.stdout.flush()


# Create image
def generate_dalle(sticker="Giraffe", size="", number=1) -> None:
    """Generates a sticker with the DALL-E model"""
    number = number_converter(number)
    for number in range(number):
        # sticker = random_sticker()
        flag = False
        for i in range(101):
            time.sleep(0.01)
            sys.stdout.write("\r" + "generating sticker" + ": [%-100s] %d%%" % ('=' * int(i/100*100), i))
            sys.stdout.flush()
            if flag == False:
                response = openai.Image.create(prompt=sticker + "as a cartoon sticker", n=1, size=size_converter(size))
                flag = True
        imageUrl = response["data"][0]["url"]
        imgData = requests.get(imageUrl).content

        randName = str(uuid.uuid4()) + ".png"

        path = "../Sticker_Generator/data/"
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)

        with open("../Sticker_Generator/data/" + randName, "wb") as handler:
            handler.write(imgData)
            handler.flush()
            handler.close()
        return randName

if __name__ == "__main__":
    generate_dalle()