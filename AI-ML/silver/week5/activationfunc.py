import tensorflow as tf


#linear activation function
def linear(x):
    return x

output = tf.keras.activations.linear(x)
#sigmoid activation function
def sigmoid(x):
    return 1/(1+np.exp(-x))

output = tf.keras.activations.sigmoid(x)

#tanh activation function
def tanh(x):
    return np.tanh(x)

output = tf.keras.activations.tanh(x)

#rectified linear unit activation function
def relu(x):
    return np.maximum(0,x)

output = tf.keras.activations.relu(x)

#leaky rectified linear unit activation function
def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

output = tf.keras.layers.LeakyReLU(alpha=0.01)(x)

#softmax activation function
def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum(axis=0)

output = tf.keras.activations.softmax(x)

