from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, Activation
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
import numpy as np
from matplotlib import pyplot as plt
from keras.utils import np_utils
import cv2
import os
from keras import backend as K
K.set_image_dim_ordering('th')
filename='mnistdatanew.txt'
def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train.reshape(x_train.shape[0], 1, 28, 28).astype('float32')

    x_test = x_test.reshape(x_test.shape[0], 1, 28, 28).astype('float32')

    x_train = x_train / 255
    x_test = x_test / 255

    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)
    
    return x_train, y_train, x_test, y_test

x_train, y_train, x_test, y_test = load_data()
num_classes = y_test.shape[1]
model = Sequential([
    Conv2D(64, kernel_size=(3,3),strides=(1, 1), padding='same', activation='relu', input_shape=((1,28, 28))),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(128, kernel_size=(3,3),strides=(1, 1), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Dropout(rate=0.2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
model.summary()
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=False)

validdatagen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True
)
datagen.fit(x_train)
validdatagen.fit(x_train)
if not os.path.exists('./{}'.format(filename) ):
    model.fit_generator(
    datagen.flow(x_train, y_train, batch_size=128), 
    steps_per_epoch=len(x_train)//128, 
    epochs=10, 
    validation_data=validdatagen.flow(x_test, y_test, batch_size=128), 
    validation_steps=len(x_test)//128
)
    model.save_weights(filename)
else:    
    model.load_weights('./{}'.format(filename) )
img_predict = cv2.imread("239new.png",0)
img2 = cv2.resize(img_predict,(28, 28))
# im_blur = cv2.GaussianBlur(img2,(5,5),0)
im,img_pred = cv2.threshold(img2,127,255,cv2.THRESH_BINARY_INV) # doan nay khong cna
img = img_pred.reshape(28,28,-1)
img_pre = img.reshape(1, 1, 28, 28).astype('float32')

img2 = img_pre/255.0
print(img2)
results = model.predict_generator(
    validdatagen.flow(img2,batch_size=1,shuffle=False),
    steps=1
)
y_pred = np.argmax(results, axis=1)
print(y_pred)
plt.imshow(img_pred, cmap='gray')