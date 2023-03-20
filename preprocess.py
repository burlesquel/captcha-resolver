import cv2 as cv
import numpy as np

def preprocess(img):
    image = img
    try:
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    except:
        pass

    try:
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    except:
        pass

    thresh = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 0)
    nparray = np.array(thresh)
    binarized = nparray / 255
    return binarized