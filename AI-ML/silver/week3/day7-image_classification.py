import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import matplotlib.pyplot as plt

# (x_train, y_train), (x_test, y_test) = cifar10.load_data()

# x_train = x_train.astype('float32') / 255.0
# x_test = x_test.astype('float32') / 255.0

# y_train = to_categorical(y_train, 10)
# y_test = to_categorical(y_test, 10)

# # print(f"Number of training samples shapes: {x_train.shape}")
# # print(f"Number of test samples shapes: {x_test.shape}")

# #define the baseline CNN model
# model = Sequential([
#     Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
#     MaxPooling2D((2, 2)),
#     Conv2D(64, (3, 3), activation='relu'),
#     MaxPooling2D((2, 2)),
#     Flatten(),
#     Dense(128, activation='relu'),
#     Dropout(0.5),
#     Dense(10, activation='softmax')
# ])

# #compile the model
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# #summary of the model
# model.summary()

# history = model.fit(x_train, y_train, epochs=10, batch_size=64, validation_split=0.2, verbose=1)#train the baseline model

# #evaluate the model on the test set
# test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
# print(f"Test accuracy: {test_accuracy:.4f}")

# #define the improved CNN model
# improved_model = Sequential([
#     Conv2D(64, (5, 5), activation='relu', input_shape=(32, 32, 3)),
#     MaxPooling2D((2, 2)),
#     Conv2D(128, (5,5), activation='relu'),
#     MaxPooling2D((2, 2)),
#     Flatten(),
#     Dense(256, activation='relu'),
#     Dropout(0.5),
#     Dense(10, activation='softmax')
# ])

# #compile the improved model with a different optimizer and learning rate
# improved_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005), loss='categorical_crossentropy', metrics=['accuracy'])

# #train the improved model
# improved_history = improved_model.fit(x_train, y_train, epochs=10, batch_size=64, validation_split=0.2, verbose=1)#evaluate the improved model on the test set

# #evaluate the improved model on the test set
# improved_test_loss, improved_test_accuracy = improved_model.evaluate(x_test, y_test, verbose=0)
# print(f"Improved Test accuracy: {improved_test_accuracy:.4f}")

# plt.figure(figsize=(10, 5))
# plt.plot(improved_history.history['loss'], label='training loss')
# plt.plot(improved_history.history['val_loss'], label='validation loss')
# plt.title('Training and Validation Loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()
# plt.show()