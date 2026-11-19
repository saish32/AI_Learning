import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer   
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
#step1 data preparation
#assuming texts contains list of text documents and labels contains corresponding sentiment labels (0 or 1)

tokenizer = Tokenizer(num_words=10000)  # Limit to top 10,000 words
tokenizer.fit_on_texts(texts)  # Fit the tokenizer on the texts
sequences = tokenizer.texts_to_sequences(texts)  # Convert texts to sequences
padded_sequences = pad_sequences(sequences, padding='post', truncating='post')  # Pad sequences to the same length

#step2 model building
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=10000, output_dim=128, input_length=padded_sequences.shape[1]),  # Embedding layer
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(128, activation='tanh')),  # Bidirectional LSTM layer with 128 units
    tf.keras.layers.Dense(64, activation='relu'),  # Dense layer with 64 units
    tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # Compile the model

#step3 model training
x_train, x_val, y_train, y_val = train_test_split(padded_sequences, labels, test_size=0.2, random_state=42)  # Split data into training and validation sets

history=model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_val, y_val))  # Train the model

#step4 model evaluation
loss, accuracy = model.evaluate(x_val, y_val)  # Evaluate the model on validation data
print(f'Validation Loss: {loss}, Validation Accuracy: {accuracy}')  # Print validation loss and accuracy

#step5 model saving
model.save('sentiment_model.h5')  # Save the trained model to a file

