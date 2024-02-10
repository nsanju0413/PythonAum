import cv2
import numpy as np

def adjust_gamma(input_image, gamma=1.0):
    table = np.array([((iteration / 255.0) ** (1.0 / gamma)) * 255 for iteration in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(input_image, table)

def read_image(path, gamma=0.75):
    output = cv2.imread(path)
    return adjust_gamma(output, gamma=gamma)
