import torch
import torch.nn as nn
import torch.nn.functional as F

class CustomLoss(nn.Module):
    def __init__(self, in_features, out_features):
        super(CustomLoss, self).__init__()
        self.linear = nn.Linear(in_features, out_features)
        self.relu= nn.ReLU()

    def forward(self, x):
        x=self.linear(x)
        x=self.relu(x)
        return x

model=nn.Sequential(
    CustomLoss(10, 5),
    nn.Linear(5, 1)
)

def __init__(self, in_features, out_features):
    super(CustomLoss, self).__init__()
    self.linear = nn.Linear(in_features, out_features)
    torch.nn.init.xavier_uniform_(self.linear.weight)  # Initialize weights using Xavier uniform initialization

class CustomLoss(nn.Module):
    def __init__(self):
        super(CustomLoss, self).__init__()

    def forward(self, input, target):
        # Custom loss calculation
        loss = F.mse_loss(input, target)  # Example: Mean Squared Error loss
        return loss

def custom_accuracy(output, target):
    # Custom accuracy calculation
    predicted = torch.round(torch.sigmoid(output))  # Example: Binary classification accuracy
    correct = (predicted == target).sum().item()
    total = target.size(0)
    accuracy = correct / total
    return accuracy

class Swish(nn.Module):
    def forward(self, x):
        return x * torch.sigmoid(x)

model=nn.Sequential(
    nn.Linear(10, 5),
    Swish(),
    nn.Linear(5, 1),
    nn.Sigmoid()
)

class Mish(nn.Module):
    def forward(self, x):
        return x * torch.tanh(F.softplus(x))

model=nn.Sequential(
    nn.Linear(10, 5),   
    Mish(),
    nn.Linear(5, 1),
    nn.Sigmoid()
)

class Gelu(nn.Module):
    def forward(self, x):
        return x * torch.sigmoid(x)

model=nn.Sequential(
    nn.Linear(10, 5),
    Gelu(),
    nn.Linear(5, 1),
    nn.Sigmoid()
)

class Dropout(nn.Module):
    def __init__(self, p=0.5):
        super(Dropout, self).__init__()
        self.p = p

    def forward(self, x):
        if self.training:
            mask = (torch.rand_like(x) > self.p).float()
            return x * mask / (1.0 - self.p)
        else:
            return x

model=nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    Dropout(p=0.5),
    nn.Linear(5, 1),
    nn.Sigmoid()
)

optimizer = torch.optim.Adam(model.parameters(), lr=0.001,weight_decay=0.01)  # L2 regularization with weight decay




        
        