import torch

x=torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

#backward pass
y=x*2
y.sum().backward()
print(x.grad)  # Output: tensor([2., 2., 2.])

#gradient descent step
with torch.no_grad():
    x -= 0.1 * x.grad
 
#detached tensor
x_detached = x.detach()

#higher-order gradients
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x * 2
gradients = torch.autograd.grad(outputs=y.sum(), inputs=x, create_graph=True)

layers=[]
for i in range(3):
    layers.append(torch.nn.Linear(10, 10))

x=torch.randn(1, 10)
for layer in layers:
    x = torch.relu(layer(x))