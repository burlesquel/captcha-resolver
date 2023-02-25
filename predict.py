from keras.models import load_model
import numpy as np
import cv2 as cv
import os
from extractletters import extract_letters
from svgtopng import svg2img

model = load_model('captcha_recognition4.h5')
labels = ['A_', 'B_', 'C_', 'D_', 'E_', 'F_', 'G_', 'H_', 'I_', 'J_', 'K_', 'L_', 'M_', 'N_', 'O_', 'P_', 'Q_', 'R_', 'S_', 'T_', 'U_', 'V_', 'W_', 'X_', 'Y_', 'Z_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def predict(captcha_svg):
    img = svg2img(captcha_svg)
    img = cv.cvtColor(img, cv.COLOR_RGBA2BGRA) # svg2img library gives the imgg in rgba format. We must convert to bgra to work better with opencv.
    letter_imgs = extract_letters(img) # Returns a list of 5 40x40 cv images.  
    result = [] # The most possible letter combination.
    for letter in letter_imgs:
        img = np.array(letter)
        reshaped_img = img.reshape((1,) + img.shape)
        predictions = model.predict(reshaped_img)
        predicted_label = np.argmax(predictions) # Returns the most possible prediction.
        predicted_label = labels[predicted_label].replace('_', '')
        print('letter: ', predicted_label)
        result.append(predicted_label)
    return result


