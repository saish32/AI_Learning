import tensorflow as tf
from tensorflow.keras.losses import mean_squared_error
#mse(mean squared error) loss function
def mse(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

output = tf.keras.losses.mean_squared_error(y_true, y_pred)

#binary cross-entropy loss function
def binary_crossentropy(y_true, y_pred):
    return tf.reduce_mean(tf.keras.losses.binary_crossentropy(y_true, y_pred))

output = tf.keras.losses.binary_crossentropy(y_true, y_pred)

#categorical cross-entropy loss function
def categorical_crossentropy(y_true, y_pred):
    return tf.reduce_mean(tf.keras.losses.categorical_crossentropy(y_true, y_pred))

output = tf.keras.losses.categorical_crossentropy(y_true, y_pred)

#sparse categorical cross-entropy loss function
def sparse_categorical_crossentropy(y_true, y_pred):
    return tf.reduce_mean(tf.keras.losses.sparse_categorical_crossentropy(y_true, y_pred))

output = tf.keras.losses.sparse_categorical_crossentropy(y_true, y_pred)

#optimizers

#sgd (stochastic gradient descent) optimizer
def sgd_optimizer(learning_rate=0.01):
    return tf.keras.optimizers.SGD(learning_rate=learning_rate)

#adam optimizer
def adam_optimizer(learning_rate=0.001):
    return tf.keras.optimizers.Adam(learning_rate=learning_rate)

#rmsprop optimizer
def rmsprop_optimizer(learning_rate=0.001):
    return tf.keras.optimizers.RMSprop(learning_rate=learning_rate)

#adagrad optimizer
def adagrad_optimizer(learning_rate=0.01):
    return tf.keras.optimizers.Adagrad(learning_rate=learning_rate)

#custom loss function 

class CustomLoss(tf.keras.losses.Loss):
    def __init__(self):
        super(CustomLoss, self).__init__()

    def call(self, y_true, y_pred):
        # Example: Mean Squared Error
        return tf.reduce_mean(tf.square(y_true - y_pred))

    custom_loss = CustomLoss()

    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)


