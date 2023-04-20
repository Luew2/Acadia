import openai
import requests
import uuid
import sys
import time
import os


# Convert size to correct format
def size_converter(size) -> str:
    """
    Converts size to correct format for OpenAI API.

    Args:
    size (str): The size of the image to be generated (e.g., "256", "512", "1024").

    Returns:
    str: The converted size in the correct format for the OpenAI API (e.g., "256x256", "512x512", "1024x1024").
    """
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
    """
    Converts number to correct format for OpenAI API.

    Args:
    number: The number of images to generate.

    Returns:
    int: The converted number in the correct format for the OpenAI API.
    """
    if number == None:
        return 1
    else:
        return number


# Create image
def generate_dalle(ROOT_DIR="", sticker="Giraffe", size="", number=1) -> None:
    """Generates a sticker with the DALL-E model.

    Args:
    ROOT_DIR (str): The root directory of the project. Default is the current working directory.
    sticker (str): The keyword to prompt DALL-E to generate a sticker.
    size (str): The size of the image to be generated (e.g., "256", "512", "1024").
    number (int): The number of images to generate.

    Returns:
    str: The filename of the generated image.
    """
    # Set OpenAI API key
    openai.api_key = os.getenv("ENV_OPENAI_KEY")
    # Convert number to correct format
    number = number_converter(number)
    for number in range(number):
        # Generate a random sticker (not implemented)
        # sticker = random_sticker()
        # Set flag to False
        flag = False
        # Iterate over progress bar
        for i in range(101):
            # Pause for 0.01 seconds
            time.sleep(0.01)
            # Print progress bar
            sys.stdout.write(
                "\r"
                + "generating sticker"
                + ": [%-100s] %d%%" % ("=" * int(i / 100 * 100), i)
            )
            sys.stdout.flush()
            # If flag is False
            if flag == False:
                # Use OpenAI API to create an image
                response = openai.Image.create(
                    prompt=sticker + "as a trendy sticker with a black background, vector art",
                    n=1,
                    size=size_converter(size),
                )
                # Set flag to True
                flag = True
        # Get image URL and data
        imageUrl = response["data"][0]["url"]
        imgData = requests.get(imageUrl).content

        # Generate a random name for the image file
        randName = str(uuid.uuid4()) + ".png"

        # Set path for the image file
        path = ROOT_DIR + "/Sticker_Generator/data/"
        isExist = os.path.exists(path)
        # If path does not exist, create it
        if not isExist:
            os.makedirs(path)

        # Save the image file
        with open(path + randName, "wb") as handler:
            handler.write(imgData)

        # Return the name of the image file
        return randName


# If this script is run directly
if __name__ == "__main__":
    # Call the generate_dalle function
    generate_dalle()
