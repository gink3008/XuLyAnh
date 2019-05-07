from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, Activation
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras import backend as K
K.set_image_dim_ordering('th')

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