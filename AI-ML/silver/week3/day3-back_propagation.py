import numpy as np
import matplotlib.pyplot as plt

# def mse_loss(y_true, y_pred):
#     return np.mean((y_true - y_pred) ** 2)

# def binary_cross_entropy_loss(y_true, y_pred):
#     epsilon = 1e-15  # to avoid log(0)
#     y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
#     return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

# y_true = np.array([[1], [0], [1], [0]])  # Example true labels
# y_pred = np.array([[0.9], [0.1], [0.8], [0.2]])  # Example predictions for MSE and bce

# mse=mse_loss(y_true, y_pred)
# bce=binary_cross_entropy_loss(y_true, y_pred)

# # print(f"MSE Loss: {mse}")
# # print(f"Binary Cross-Entropy Loss: {bce}")

# def mse_gradient(y_true, y_pred):
#     return 2 * (y_pred - y_true) / y_true.size

# def bce_gradient(y_true, y_pred):
#     epsilon = 1e-15  # to avoid division by zero
#     y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
#     return (y_pred - y_true) / (y_pred * (1 - y_pred) * y_true.size)

# mse_grad=mse_gradient(y_true, y_pred)
# bce_grad=bce_gradient(y_true, y_pred)

# # print(f"MSE Gradient:\n{mse_grad}")
# # print(f"Binary Cross-Entropy Gradient:\n{bce_grad}")

# predictions=np.linspace(0, 1, 100)
# true_label=1
# mse_losses=[(true_label- p)**2 for p in predictions]
# bce_losses=[-true_label * np.log(max(p, 1e-15)) - (1 - true_label) * np.log(max(1 - p, 1e-15)) for p in predictions]

# plt.figure(figsize=(12, 8))
# plt.plot(predictions, mse_losses, label='MSE Loss', color='blue')
# plt.plot(predictions, bce_losses, label='Binary Cross-Entropy Loss', color='orange')
# plt.xlabel('Predicted Probability')
# plt.ylabel('Loss')
# plt.title('Loss Functions')
# plt.legend()
# plt.grid(True)
# plt.show()


