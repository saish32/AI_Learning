import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence 

#load and process the IMDB dataset
max_features = 10000 #number of words to consider as features
maxlen = 500 #cut texts after this number of words (among top max_features most common words)
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

model= models.Sequential([
    layers.Embedding(max_features, 32),
    layers.SimpleRNN(32),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.1) #train the model
test_loss, test_acc = model.evaluate(x_test, y_test) #evaluate the model on the test data
print(f'Test accuracy: {test_acc}') #print the test accuracy
print(f'Test loss: {test_loss}') #print the test loss