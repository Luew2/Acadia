import os
import cv2
import numpy as np
import onnxruntime as ort


def background_remover_ai(sticker, ROOT_DIR=""):
    """
    Remove background from an input image using U2Net and save the result with transparent background.

    Args:
    sticker (str): Name of the image file.
    ROOT_DIR (str): Path to the root directory. Defaults to "".

    Returns:
    None
    """

    # Set the directory to the data folder
    dir = os.path.join(ROOT_DIR + "/Sticker_Generator/data/")

    # Load the input image
    input_path = os.path.join(dir, sticker)
    input_img = cv2.imread(input_path)
    input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)

    # Create the ONNX Runtime session
    script_dir = os.path.dirname(os.path.realpath(__file__))
    onnx_path = os.path.join(script_dir, "u2net.onnx")
    ort_session = ort.InferenceSession(onnx_path)

    # Preprocess the input image
    input_img = cv2.resize(input_img, (320, 320))
    input_img = input_img.astype(np.float32) / 255.0
    input_img = np.transpose(input_img, (2, 0, 1))
    input_img = np.expand_dims(input_img, axis=0)

    # Run the U2Net model on the input image
    output = ort_session.run(None, {'input': input_img})[0]
    output = output.squeeze()
    output = cv2.resize(output, (input_img.shape[3], input_img.shape[2]))
    output = (output * 255).astype(np.uint8)

    # Check if the image has three channels before converting to grayscale
    if output.shape[-1] == 3:
        gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
    else:
        gray = output

    # Threshold the grayscale image to create a binary mask
    _, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

    # Resize the mask to match the dimensions of the input image
    mask = cv2.resize(mask, (input_img.shape[3], input_img.shape[2]))

    # Convert the mask to uint8

    mask = mask.astype(np.uint8)

    # Save the binary mask
    mask_path = os.path.join(dir, "MASK_" + sticker.split(".")[0] + ".png")
    cv2.imwrite(mask_path, mask)

    # Perform the bitwise operation to remove the background
    input_img_uint8 = (input_img.squeeze().transpose(1, 2, 0) * 255).astype(np.uint8)
    input_img_bgr = cv2.cvtColor(input_img_uint8, cv2.COLOR_RGB2BGR)
    foreground = cv2.bitwise_and(input_img_bgr, input_img_bgr, mask=mask)

    # Merge the foreground with the alpha channel
    output = cv2.cvtColor(foreground, cv2.COLOR_BGR2BGRA)
    output[:, :, 3] = mask

    # Save the image with transparent background
    output_path = os.path.join(dir, "NO-BACKGROUND_" + sticker.split(".")[0] + ".png")
    cv2.imwrite(output_path, output)


if __name__ == "__main__":
    # Example usage
    name = "bc2347ce-3353-4c99-a01d-63e3ab3024f2.png"
    background_remover_ai(name, "")
