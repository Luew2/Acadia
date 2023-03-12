import cv2
import numpy as np
import os


def salt_pepper_noise(edge_img):
    """
    Apply salt and pepper noise reduction to an edge image.

    Args:
    edgeImg (numpy.ndarray): The input edge image.

    Returns:
    None
    """
    count = 0
    last_median = edge_img
    median = cv2.medianBlur(edge_img, 3)
    while not np.array_equal(last_median, median):
        zeroed = np.invert(np.logical_and(median, edge_img))
        edge_img[zeroed] = 0
        count = count + 1
        if count > 70:
            break
        last_median = median
        median = cv2.medianBlur(edge_img, 3)


def fing_significant_contour(edge_img):
    """
    Find the largest contour in an edge image.

    Args:
    edge_img (numpy.ndarray): The input edge image.

    Returns:
    numpy.ndarray: The largest contour.
    """
    # contours, hierarchy = cv2.findContours(
    #     edge_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    # )

    contours, hierarchy = cv2.findContours(
        edge_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )

    # Find level 1 contours
    level1Meta = []
    for contour_index, tupl in enumerate(hierarchy[0]):
        # Filter the ones without parent
        if tupl[3] == -1:
            tupl = np.insert(tupl.copy(), 0, [contour_index])
            level1Meta.append(tupl)

    # From among them, find the contours with large surface area.
    contours_with_area = []
    for tupl in level1Meta:
        contour_index = tupl[0]
        contour = contours[contour_index]
        area = cv2.contourArea(contour)
        contours_with_area.append([contour, area, contour_index])
    contours_with_area.sort(key=lambda meta: meta[1], reverse=True)
    largest_contour = contours_with_area[0][0]
    return [largest_contour]


def backround_remover(sticker, ROOT_DIR=""):
    """
    Remove background from an input image using OpenCV and save the result.

    Args:
    sticker (str): Name of the image file.
    ROOT_DIR (str): Path to the root directory. Defaults to "".

    Returns:
    None
    """

    # Set the directory to the data folder
    dir = os.path.join(ROOT_DIR + "/Sticker_Generator/data/")

    # Load the input image
    image_vec = cv2.imread(os.path.join(dir, sticker), 1)

    # Apply Gaussian blur
    g_blurred = cv2.GaussianBlur(image_vec, (5, 5), 0)
    blurred_float = g_blurred.astype(np.float32) / 255.0
    # cv2.imwrite("blur.jpg", g_blurred)

    # Detect edges in the image
    edge_detector = cv2.ximgproc.createStructuredEdgeDetection(
        ROOT_DIR + "/Transformer/model.yml"
    )
    edges = edge_detector.detectEdges(blurred_float) * 255.0

    # Save the raw edges image
    # cv2.imwrite("edge-raw.jpg", edges)

    # Add salt and pepper noise to the edges image
    edges_ = np.asarray(edges, np.uint8)
    salt_pepper_noise(edges_)
    # cv2.imwrite("edge.jpg", edges_)

    # Find the significant contour in the edges image
    contour = fing_significant_contour(edges_)

    # Draw the contour on the original image
    contourImg = np.copy(image_vec)
    cv2.drawContours(contourImg, contour, 0, (0, 255, 0), 2, cv2.LINE_AA, maxLevel=-1)
    cv2.imwrite("contour.jpg", contourImg)

    # Create a mask of the contour
    mask = np.zeros_like(edges_)
    cv2.fillPoly(mask, contour, 255)

    # Dilate the mask to create a sure foreground area
    map_fg = cv2.erode(mask, np.ones((5, 5), np.uint8), iterations=10)

    # Mark initial mask as "probably background" and mapFg as sure foreground
    trimap = np.copy(mask)
    trimap[mask == 0] = cv2.GC_BGD
    trimap[mask == 255] = cv2.GC_PR_BGD
    trimap[map_fg == 255] = cv2.GC_FGD

    # Visualize the trimap
    trimap_print = np.copy(trimap)
    trimap_print[trimap_print == cv2.GC_PR_BGD] = 128
    trimap_print[trimap_print == cv2.GC_FGD] = 255

    # Apply GrabCut algorithm
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)
    mask, bgd_model, fgd_model = cv2.grabCut(
        image_vec,
        trimap,
        None,
        bgd_model,
        fgd_model,
        iterCount=5,
        mode=cv2.GC_INIT_WITH_MASK,
    )

    # Create a mask where 0 and 2 are background and 1 and 3 are foreground
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")

    # Apply the mask to the image
    result = image_vec * mask2[:, :, np.newaxis]

    # Save the image with the removed background
    cv2.imwrite(dir + "/NO-BACKGROUND_" + sticker, result)


if __name__ == "__main__":
    # Example usage
    name = ""
    backround_remover(name, "")
