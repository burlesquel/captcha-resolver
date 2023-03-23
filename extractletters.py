from constants import six_character_coordinates
# Find the each letter portion from the image by fixed coordinations.
# Extracts the letter in 40x40 format, downscales the whole image to 250x150 if its smaller than that.
import cv2 as cv

def extract_letters(img):
    downscaled = cv.resize(img, (358, 65))
    letters = []
    for coord in six_character_coordinates:
        x,y = coord
        letter = downscaled[x:x+40, y:y+40]
        letters.append(letter)
    return letters

