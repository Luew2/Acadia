import cv2
import numpy as np
import os
import random


def backround_remover(sticker, ROOT_DIR=""):
    """Remove background from an input image using OpenCV and save the result.

    Args:
    sticker (str): Name of the image file.
    ROOT_DIR (str): Path to the root directory. Defaults to "".

    Returns:
    None
    """

    dir = os.path.join(ROOT_DIR + "/Sticker_Generator/data/")

    # Load image
    img = cv2.imread(os.path.join(dir, sticker))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold input image as mask
    mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]

    # Negate mask
    mask = 255 - mask

    # Apply morphology to remove isolated extraneous noise
    # Use borderconstant of black since foreground touches the edges
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Anti-alias the mask -- blur then stretch
    # Blur alpha channel
    mask = cv2.GaussianBlur(
        mask, (0, 0), sigmaX=2, sigmaY=2, borderType=cv2.BORDER_DEFAULT
    )

    # Linear stretch so that 127.5 goes to 0, but 255 stays 255
    mask = (2 * (mask.astype(np.float32)) - 255.0).clip(0, 255).astype(np.uint8)

    # Put mask into alpha channel
    result = img.copy()
    result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
    result[:, :, 3] = mask

    # Save resulting masked image
    cv2.imwrite(dir + "/NO-BACKGROUND_" + sticker, result)

    print("done")


if __name__ == "__main__":
    # Example usage
    name = "ba9bd6b4-c8da-42eb-8c1b-ecbac9d88624.png"
    backround_remover(name)
