import numpy as np
import os
import cv2 as cv
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import  Dense, Flatten, Conv2D, MaxPool2D
from keras.models import load_model
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

print('modules imported')

img_size = (40,40)

classes=['A_', 'B_', 'C_', 'D_', 'E_', 'F_', 'G_', 'H_', 'I_', 'J_', 'K_', 'L_', 'M_', 'N_', 'O_', 'P_', 'Q_', 'R_', 'S_', 'T_', 'U_', 'V_', 'W_', 'X_', 'Y_', 'Z_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+']

train_path = 'dataset'

images = []
labels = []

print('preparing data')
# It reads the each image in each letter folder, appends to the list with labels after applying adaptive threshold and binarization and converting to np array.
for i, cls in enumerate(classes):
    class_path = os.path.join(train_path, cls)
    print(i ,'/', len(classes))
    for image_filename in os.listdir(class_path):
        image_path = os.path.join(class_path, image_filename)
        image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
        image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 0)
        image_array = np.array(image, dtype=np.float32)
        image_array /= 255.0 # Converts each pixel value to either 0 or 1 by their distance to both.
        images.append(image_array)
        labels.append(i)

images = np.array(images)
labels = np.array(labels)

labels = to_categorical(labels, num_classes=len(classes)) # Converts labels into [0,0,0,0....1,0,0,0...] format

images, labels = shuffle(images, labels, random_state=42) # Shuffles images and labels respective to each other

train_images, val_images, train_labels, val_labels = train_test_split(images, labels, test_size=0.2) # Generates train and validation batches.

print('data prepared')

print('creating model')

model = Sequential([
    Conv2D(filters=32, kernel_size=(3,3), activation='relu', padding='same', input_shape=(40,40,1)),
    MaxPool2D(pool_size=(2,2),strides=2),
    Conv2D(filters=64, kernel_size=(3,3), activation='relu', padding='same'),
    MaxPool2D(pool_size=(2,2),strides=2),
    Flatten(),
    Dense(units=len(classes), activation='softmax')
])

# model = load_model('captcha_recognition2.h5')

print('model is ready')

model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images,  train_labels, batch_size=32, validation_data=(val_images, val_labels), epochs=10, verbose=2)

model.save('test.h5')





# from keras.models import load_model
# model = load_model('captcha_recognition.h5')
# model.fit(x=train_batches, epochs=10, verbose=2)
# model.save('captcha_recognition2.h5')