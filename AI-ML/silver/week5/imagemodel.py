import tensorflow as tf
from tensorflow.keras import Sequential, Model, layers
from tensorflow.keras.datasets import mnist

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values and add the channel dimension expected by Conv2D.
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]

#building a simple CNN model for image classification
model = Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),  # Convolutional layer with 32 filters
    layers.MaxPooling2D((2, 2)),  # Max pooling layer
    layers.Conv2D(64, (3, 3), activation='relu'),  # Convolutional layer with 64 filters
    layers.MaxPooling2D((2, 2)),  # Max pooling layer
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),  # Max pooling layer
    layers.Flatten(),  # Flatten the output
    layers.Dense(128, activation='relu'),  # Dense layer with 128 units
    layers.Dense(10, activation='softmax')  # Output layer for 10 classes
])

#compile the model
# MNIST labels are integer class IDs, so use the sparse categorical loss.
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history=model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test))  # Train the model

#evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)  # Evaluate the model on validation data
print(f'Validation Loss: {loss}, Validation Accuracy: {accuracy}')  # Print validation loss and accuracy

#save the model
model.save('image_classification_model.h5')  # Save the trained model to a file

