from keras import *
from tensorflow import keras
import tensorflow as tf
import numpy as np

model = keras.models.load_model('model.h5')
while True:
    x = int(input("nombre : "))
    print("prediction : ", str(model.predict([x])))