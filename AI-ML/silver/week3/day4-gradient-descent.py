import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import torch
import torch.nn as nn
import torch.optim as optim

x=2*np.random.rand(100,1)
y=4+3*x+np.random.randn(100,1)

# plt.scatter(x,y,color='blue')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

m=100
iterations=1000
theta=np.random.randn(2,1)
learning_rate=0.1

x_bias=np.c_[np.ones((m,1)),x]

for iterations in range(iterations):
    gradients=2/m*x_bias.T.dot(x_bias.dot(theta)-y)
    theta=theta-learning_rate*gradients

print(theta)

x_tensor=tf.constant(x,dtype=tf.float32)
y_tensor=tf.constant(y,dtype=tf.float32)

#define linear model
class LinearModel(tf.Module):
    def __init__(self):
        self.weights=tf.Variable(tf.random.normal([1]),name='weights')
        self.bias=tf.Variable(tf.random.normal([1]),name='bias')

    def __call__(self,x):
        return self.weights*x+self.bias

def mse_loss(y_true,y_pred):
    return tf.reduce_mean(tf.square(y_true-y_pred))

#train with sgd
model=LinearModel()
optimizer=tf.optimizers.SGD(learning_rate=0.1)

# for epoch in range(100):
#     with tf.GradientTape() as tape:
#         y_pred=model(x_tensor)
#         loss=mse_loss(y_tensor,y_pred)
#     gradients=tape.gradient(loss,[model.weights,model.bias])
#     optimizer.apply_gradients(zip(gradients,[model.weights,model.bias]))
#     if epoch%10==0:
#         print(f"Epoch {epoch}: Loss: {loss.numpy()}")

x_torch=torch.tensor(x,dtype=torch.float32)
y_torch=torch.tensor(y,dtype=torch.float32)

#define linear model
class LinearModelTorch(nn.Module):
    def __init__(self):
        super(LinearModelTorch,self).__init__()
        self.linear=nn.Linear(1,1)

    def forward(self,x):
        return self.linear(x)

model_torch=LinearModelTorch()
criterion=nn.MSELoss()
optimizer_torch=optim.SGD(model_torch.parameters(),lr=0.1)

# for epoch in range(100):
#     optimizer_torch.zero_grad()
#     y_pred=model_torch(x_torch)
#     loss=criterion(y_pred,y_torch)
#     loss.backward()
#     optimizer_torch.step()
#     if epoch%10==0:
#         print(f"Epoch {epoch}: Loss: {loss.item()}")

