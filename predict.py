from keras.models import load_model
# from keras.applications import vgg16
import numpy as np
import cv2 as cv
import os
from extractletters import extract_letters

model = load_model('captcha_recognition4.h5')
labels = ['A_', 'B_', 'C_', 'D_', 'E_', 'F_', 'G_', 'H_', 'I_', 'J_', 'K_', 'L_', 'M_', 'N_', 'O_', 'P_', 'Q_', 'R_', 'S_', 'T_', 'U_', 'V_', 'W_', 'X_', 'Y_', 'Z_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def predict(captcha):

    letter_imgs = extract_letters(captcha)
    result = []
    for letter in letter_imgs:
        img = np.array(letter)
        reshaped_img = img.reshape((1,) + img.shape)
        predictions = model.predict(reshaped_img)
        predicted_label = np.argmax(predictions)
        predicted_label = labels[predicted_label]
        print('letter: ', predicted_label)
        cv.waitKey(0)
        result.append(predicted_label)
    return result



# captchas = os.listdir('test')

# for captcha in captchas:
#     captcha_img = cv.imread('test/' + captcha)
#     result = predict(captcha_img)
#     print(result)
#     cv.imshow('captcha', captcha_img)
#     cv.waitKey(0)

