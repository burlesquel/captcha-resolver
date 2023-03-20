
import cv2 as cv
import matplotlib.pyplot as plt
from constants import five_character_coordinates, four_character_coordinates, math_character_coordinates
from raw_predict import raw_predict
from utils import find_highest_averaged_predictions

all_coordinates = five_character_coordinates + \
    four_character_coordinates + math_character_coordinates
all_coordinates = sorted(all_coordinates, key=lambda x: x[1])

coordinate_dictionary = {
    "five": five_character_coordinates,
    "four": four_character_coordinates,
    "math": math_character_coordinates
}

def predict(image=None, mode=None):
    img = None
    if True:
        img = image
    else:
        img = cv.imread('captchas/fourcaptcha.png', cv.IMREAD_GRAYSCALE)
    img = cv.resize(img, (250, 150))
    if not mode:
        predictions = []
        for coordinate_plan in [five_character_coordinates, four_character_coordinates, math_character_coordinates]:
            for coord in coordinate_plan:
                y, x = coord
                letter = img[y: y + 40, x: x + 40]  # Crop
                print('looking for ', coord)
                # plt.imshow(letter)
                # plt.show()
                prediction = raw_predict(letter)
                predictions.append(prediction)
        possible_predictions = find_highest_averaged_predictions(
            [predictions[:5], predictions[5:9], predictions[9:]])
        print(possible_predictions)
        print([prediction[0] for prediction in possible_predictions])
        return [prediction[0] for prediction in possible_predictions]
    elif mode == "five" or mode == "four" or mode=="math":
        predictions = []
        for coord in coordinate_dictionary[mode]:
            y, x = coord
            letter = img[y: y + 40, x: x + 40]  # Crop
            prediction = raw_predict(letter)
            predictions.append(prediction)
        print([prediction[0] for prediction in predictions])
        return [prediction[0] for prediction in predictions]



# predict(mode="four")
