import numpy as np
from preprocess import preprocess
from keras.models import load_model
from constants import labels
model = load_model('model.h5')

def raw_predict(letter):
    preprocessed_img = preprocess(letter)
    reshaped_img = preprocessed_img.reshape((1,) + preprocessed_img.shape)
    predictions = model.predict(reshaped_img, verbose=1)
    predicted_label_index = np.argmax(predictions)
    confidence = predictions[0][predicted_label_index]
    predicted_label = labels[predicted_label_index].replace('_', '')
    print('letter: ', predicted_label, ' with confidence of %', confidence * 100)
    return predicted_label, confidence