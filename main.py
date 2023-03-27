
import cv2 as cv
from constants import six_character_coordinates
from raw_predict import raw_predict

def predict(image=None):
    img = image
    img = cv.resize(img, (358, 65))
    predictions = []
    for coord in six_character_coordinates:
        x,y = coord
        letter = img[y:y + 40, x:x + 40]  # Crop
        prediction = raw_predict(letter)
        predictions.append(prediction)
    print([prediction[0] for prediction in predictions])
    return [prediction[0] for prediction in predictions]
