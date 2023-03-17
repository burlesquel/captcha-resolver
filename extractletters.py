import os
import cv2 as cv
import matplotlib.pyplot as plt

character_coordinates = [(63, 22), (63, 62), (63, 105), (63, 145), (63, 185)]
math_character_coordinate = [(60, 42), (60, 102), (60, 165)]
# Find the each letter portion from the image by fixed coordinations.
# Extracts the letter in 40x40 format, downscales the whole image to 250x150 if its smaller than that.


def extract_letters(img, type="normal", dataset_mode=False):
    if type == "normal":
        img = cv.resize(img, (250, 150))
        letters = []  # List of 40x40 cv images.
        for coordinate in character_coordinates:
            y, x = coordinate
            letter = img[y: y + 40, x: x + 40]  # Generate
            letter = cv.cvtColor(letter, cv.COLOR_BGR2GRAY)
            # Applying adaptive threshold due to strong color variation.
            letter = cv.adaptiveThreshold(
                letter, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 0)
            letters.append(letter)
        return letters
    elif type == "math":
        img = cv.resize(img, (250, 150))
        if dataset_mode:  # in dataset_mode we only get the + sign in the middle to get + samples
            chars = []
            for coordinate in math_character_coordinate:
                y, x = coordinate
                symbol = img[y: y + 40, x: x + 40]  # Generate
                symbol = cv.cvtColor(symbol, cv.COLOR_BGR2GRAY)
                # Applying adaptive threshold due to strong color variation.
                symbol = cv.adaptiveThreshold(
                    symbol, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 0)
                chars.append(symbol)
            return chars
        else:
            chars = []
            for coordinate in math_character_coordinate:
                y, x = coordinate
                char = img[y: y + 40, x: x + 40]  # Generate
                char = cv.cvtColor(char, cv.COLOR_BGR2GRAY)
                # Applying adaptive threshold due to strong color variation.
                char = cv.adaptiveThreshold(
                    char, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 0)
                chars.append(char)
            print('chars length: ', len(chars))
            return chars
