import tensorflow as tf
from tensorflow.keras import Sequential, Model
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D

# model = Sequential([
#     Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
#     MaxPooling2D(pool_size=(2, 2)),
#     Conv2D(64, kernel_size=(3, 3), activation='relu'),
#     MaxPooling2D(pool_size=(2, 2)),
#     Flatten(),
#     Dense(128, activation='relu'),
#     Dense(10, activation='softmax')
# ])

# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# model.summary()
#define the input layer
inputs=Input(shape=(28, 28, 1))
#define the convolutional and pooling layers
conv1=Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1))
pool1=MaxPooling2D(pool_size=(2, 2))
conv2=Conv2D(64, kernel_size=(3, 3), activation='relu')
pool2=MaxPooling2D(pool_size=(2, 2))
#define the flatten and dense layers
flatten=Flatten()
dense1=Dense(128, activation='relu')
dense2=Dense(10, activation='softmax')

#define the model by connecting the layers
x=conv1(inputs)
x=pool1(x)
x=conv2(x)
x=pool2(x)
x=flatten(x)
x=dense1(x)
outputs=dense2(x)

model=Model(inputs=inputs, outputs=outputs)

#compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#model summary to see the architecture
model.summary()