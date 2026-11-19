import torch
import torch.nn as nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torch.nn.functional as F

# #defien transformations for the dataset
# transform=transforms.Compose([
#     transforms.ToTensor(),
#     transforms.Normalize((0.5,),(0.5,))
# ])

# #load the MNIST dataset
# train_dataset=datasets.MNIST(root='./data', train=True, download=True, transform=transform)
# test_dataset=datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# # create data loaders
# train_loader=DataLoader(train_dataset, batch_size=32, shuffle=True)
# test_loader=DataLoader(test_dataset, batch_size=32, shuffle=False)

# print(f"Number of training samples: {len(train_dataset)}")
# print(f"Number of test samples: {len(test_dataset)}")

# #define the neural network model
# class MNISTClassifier(nn.Module):
#     def __init__(self):
#         super(MNISTClassifier, self).__init__()
#         self.flatten=nn.Flatten()
#         self.fc1=nn.Linear(28*28,128)
#         self.fc2=nn.Linear(128,64)
#         self.fc3=nn.Linear(64,10)


#     def forward(self,x):
#         x=self.flatten(x)
#         x=F.relu(self.fc1(x))
#         x=F.relu(self.fc2(x))
#         output=self.fc3(x)
#         return output

# model=MNISTClassifier()
# # print(model)

# #define the loss function and optimizer
# criterion=nn.CrossEntropyLoss()
# optimizer=torch.optim.Adam(model.parameters(), lr=0.001)

# #training loop
# def train_model(model, train_loader, criterion, optimizer, epochs=5):
#     model.train()
#     for epoch in range(epochs):
#         running_loss=0.0
#         for images, labels in train_loader:
#             optimizer.zero_grad()
# loaded_model=MNISTClassifier()
# loaded_model.load_state_dict(torch.load('mnist_model.pth'))

# #verify the loaded model's performance
# evaluate_model(loaded_model, test_loader)#             outputs=model(images)
#             loss=criterion(outputs, labels)
#             loss.backward()
#             optimizer.step()
#             running_loss+=loss.item()
#         print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss/len(train_loader):.4f}")

# train_model(model, train_loader, criterion, optimizer, epochs=10)

# def evaluate_model(model, test_loader):
#     model.eval()
#     correct=0
#     total=0
#     with torch.no_grad():
#         for images, labels in test_loader:
#             outputs=model(images)
#             _, predicted=torch.max(outputs.data,1)
#             total+=labels.size(0)
#             correct+=(predicted==labels).sum().item()
#     accuracy=100*correct/total
#     print(f"Test Accuracy: {accuracy:.2f}%")

# evaluate_model(model, test_loader)

# #save the model
# torch.save(model.state_dict(), 'mnist_model.pth')

#reload the model


# #update the model to a new learning rate 
# optimizer=torch.optim.Adam(model.parameters(), lr=0.0001)
# train_model(model, train_loader, criterion, optimizer, epochs=5)
# evaluate_model(model, test_loader)





