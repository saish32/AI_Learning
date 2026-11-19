import numpy as np
import matplotlib.pyplot as plt

# #define activation functions
# def sigmoid(z):
#     return 1 / (1 + np.exp(-z))

# def tanh(z):
#     return np.tanh(z)

# def relu(z):
#     return np.maximum(0, z)

# def softmax(z):
#     exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))  # for numerical stability
#     return exp_z / np.sum(exp_z, axis=1, keepdims=True)

# def forward_pass(x, weights, biases, activation_functions):
#     z=np.dot(weights,x)+biases
#     a=activation_functions(z)
#     return a

# x=np.array([[0.5], [0.2]])  # Example input
# weights=np.array([[0.2, 0.4,], [0.6, 0.8]])  # Example weights
# biases=np.array([[0.1], [0.2]])  # Example biases

# activation={
#     'sigmoid': sigmoid,
#     'tanh': tanh,
#     'relu': relu,
#     'softmax': softmax
# }

# for name, func in activation.items():
#     output=forward_pass(x,weights,biases,func)
#     print(f"Output using {name} activation function:\n{output}\n")


# z=np.linspace(-10, 10, 100)
# plt.figure(figsize=(12, 8))
# plt.plot(z, sigmoid(z), label='Sigmoid', color='blue')
# plt.plot(z, tanh(z), label='Tanh', color='orange')
# plt.plot(z, relu(z), label='ReLU', color='green')
# plt.plot(z, softmax(z.reshape(-1, 1)), label='Softmax', color='red')  # Softmax is applied to a 2D array
# plt.xlabel('Input')
# plt.ylabel('Output')
# plt.title('Activation Functions')
# plt.legend()
# plt.grid(True)
# plt.show()