from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
import numpy as np

# Sample data (e.g., points in 5D space)
x=np.array([[1, 2, 3, 4, 5], [1, 4, 5, 6, 7], [1, 0, 1, 2, 3],
                 [4, 2, 3, 4, 5], [4, 4, 5, 6, 7], [4, 0, 1, 2, 3]])


# Define the input dimension
input_dim = x.shape[1]  # Number of features in the input data
encoding_dim = 2  # Dimension of the encoded representation

#encoder
input_layer = Input(shape=(input_dim,))
encoded = Dense(encoding_dim, activation='relu')(input_layer)

#decoder
decoded = Dense(input_dim, activation='sigmoid')(encoded)

# Create the autoencoder model
autoencoder = Model(input_layer, decoded)
#compile the autoencoder model
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

#train the autoencoder
autoencoder.fit(x, x, epochs=100, batch_size=2, shuffle=True, validation_split=0.2, verbose=0)

#get the encoded representation of the input data
encoder = Model(input_layer, encoded)
x_encoded = encoder.predict(x)

print("Original data:\n", x)
print("Encoded representation:\n", x_encoded)
