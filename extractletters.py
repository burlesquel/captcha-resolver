import os
import cv2 as cv
import matplotlib.pyplot as plt

character_coordinates = [(63, 22), (63, 62), (63, 105), (63, 145), (63, 185)]

# Find the each letter portion from the image by fixed coordinations. 
# Extracts the letter in 40x40 format, downscales the whole image to 250x150 if its smaller than that.

def extract_letters(img):
    img = cv.resize(img, (250, 150))
    letters = [] # List of 40x40 cv images.
    for coordinate in character_coordinates:
        y, x = coordinate
        letter = img[y : y + 40, x : x + 40] # Generate
        letter = cv.cvtColor(letter, cv.COLOR_BGR2GRAY)
        letter = cv.adaptiveThreshold(letter, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 0) # Applying adaptive threshold due to strong color variation.
        letters.append(letter)
    return letters

