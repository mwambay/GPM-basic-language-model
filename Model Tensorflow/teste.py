from keras import *
from tensorflow import keras
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

model = Sequential()
model.add(layers.Dense(units=3, input_shape=[1]))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))

model.add(layers.Dense(units=1))

entree = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
sortie = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50]
model.compile(loss='mean_squared_error',optimizer='adam')
history = model.fit(x=entree, y=sortie, epochs=5000)
model.save('model.h5')
print("Model saved to disk")

# Trace les courbes de perte
plt.plot(history.history['loss'])
plt.title('Courbe de perte')
plt.xlabel('Époque')
plt.ylabel('Perte')
plt.show()
while True:
    x = int(input("nombre : "))
    if x == 0 : break
    print("prediction : ", str(model.predict([x])))
    
    
