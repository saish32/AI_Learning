import tensorflow as tf
from tensorflow.keras import Sequential, Model, layers

#building a simple RNN model for time series prediction
model = Sequential([
    layers.LSTM(50, return_sequences=True, input_shape=(28, 28)),
    layers.LSTM(50),
    layers.Dense(1, activation='sigmoid')
])

#compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#model training
history=model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))  # Train the model

#model evaluation
loss, accuracy = model.evaluate(x_test, y_test)  # Evaluate the model on validation data
print(f'Validation Loss: {loss}, Validation Accuracy: {accuracy}')  # Print validation loss and accuracy

#model saving
model.save('timeseries_model.h5')  # Save the trained model to a file