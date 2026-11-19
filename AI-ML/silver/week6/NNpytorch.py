import torch
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc1=nn.Linear(10, 50)#first fully connected layer
        self.fc2=nn.Linear(50, 20)#second fully connected layer
        self.fc3=nn.Linear(20, 1)#output layer

    def forward(self, x):
        x=torch.relu(self.fc1(x))#apply ReLU activation function after first layer
        x=torch.relu(self.fc2(x))#apply ReLU activation function after second layer
        x=self.fc3(x)#output layer without activation function
        return x

#initialize the model
model=NeuralNetwork()
input_data=torch.randn(1, 10)#random input data
output=model(input_data)#forward pass through the model
print(output)

#forward pass through the model with a batch of data
batch_input=torch.randn(5, 10)#random batch input data
batch_output=model(batch_input)#forward pass through the model with batch input

#backward pass and optimization
criterion=nn.MSELoss()#mean squared error loss
optimizer=torch.optim.SGD(model.parameters(), lr=0.01)#stochastic gradient descent optimizer

#loss function and backward pass
target=torch.randn(5, 1)#random target data
loss=criterion(batch_output, target)
loss.backward()
optimizer.step()

#optimizer loop

for epoch in range(100):#training loop for 100 epochs
    optimizer.zero_grad()#zero the gradients
    batch_output=model(batch_input)#forward pass
    loss=criterion(batch_output, target)#compute loss
    loss.backward()#backward pass
    optimizer.step()#update weights


