import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

model = Sequential([
    Flatten(input_shape=(28, 28)),
    #input layer flattens the 28x28 pixel images into a 1D array of 784 pixels
    Dense(128, activation='relu'),
    #hidden layer with 128 neurons and ReLU activation function
    Dense(10, activation='softmax')
    #output layer with 10 neurons (one for each class) and softmax activation function
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#print the model summary to see the architecture
model.summary()

#train the model on the training data
model.fit(x_train, y_train, epochs=5,batch_size=32, validation_data=(x_test, y_test))

#evaluate the model on the test data
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Test accuracy: {test_acc}")
print(f"Test loss: {test_loss}")

#make predictions on new data
predictions = model.predict(test_images)