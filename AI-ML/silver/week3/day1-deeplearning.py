from tensorflow.keras.datasets import mnist, cifar10
import tensorflow as tf
import torch
import torch.nn as nn
import matplotlib.pyplot as plt



# Load the MNIST dataset
(x_train_mnist, y_train_mnist), (x_test_mnist, y_test_mnist) = mnist.load_data()
# print("MNIST dataset loaded:")
# print(f"training dataset shape: {x_train_mnist.shape}, testing dataset shape: {x_test_mnist.shape}")

# Load the CIFAR-10 dataset
(x_train_cifar, y_train_cifar), (x_test_cifar, y_test_cifar) = cifar10.load_data()
# print("CIFAR-10 dataset loaded:")
# print(f"training dataset shape: {x_train_cifar.shape}, testing dataset shape: {x_test_cifar.shape}")

#define a dense layer using tensorflow.keras.layers.Dense
# dense_layer = tf.keras.layers.Dense(units=128, activation='relu')
# print("Dense layer defined:")
# print(dense_layer)

#dafine a dense layer using torch.nn.Linear
# linear_layer = nn.Linear(in_features=10, out_features=5)
# print("Linear layer defined:")
# print(linear_layer)

#visualize the mnit dataset using matplotlib
# plt.imshow(x_train_mnist[0], cmap='gray')
# plt.title(f"Label: {y_train_mnist[0]}")
# plt.show()

# #visualize the cifar-10 dataset using matplotlib
# plt.imshow(x_train_cifar[0], cmap='gray')
# plt.title(f"Label: {y_train_cifar[0]}")
# plt.show()