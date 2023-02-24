import os
import cv2 as cv
import matplotlib.pyplot as plt

character_coordinates = [(63, 22), (63, 62), (63, 105), (63, 145), (63, 185)]


def extract_letters(img):
    img = cv.resize(img, (250, 150))
    letters = []
    for coordinate in character_coordinates:
        y, x = coordinate
        letter = img[y : y + 40, x : x + 40]
        letter = cv.cvtColor(letter, cv.COLOR_BGR2GRAY)
        letter = cv.adaptiveThreshold(
            letter, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 0
        )
        letters.append(letter)
    return letters


# dataset = "dataset"


# for letter in os.listdir("captchas"):
#     print(letter)
#     for captcha in os.listdir("captchas/" + letter):
#         img = cv.imread("captchas/" + letter + "/" + captcha)
#         letters = extract_letters(img)
#         if not os.path.exists("dataset/" + letter):
#             os.makedirs("dataset/" + letter)
#         for letterimg in letters:
#             cv.imwrite("dataset/" + letter + "/" + randomString(5) + '.png', letterimg)
