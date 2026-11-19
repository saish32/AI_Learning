import torch
import numpy as np

#create a tensor from a list
data = [[1, 2], [3, 4]]
tensor = torch.tensor(data)

#create a tensor from a numpy array
np_array = np.array(data)
tensor_from_np = torch.from_numpy(np_array)

#create a tensor with random values
random_tensor = torch.rand(2, 2)
normal_tensor = torch.randn(2, 2)

#zeros and ones
zeros_tensor = torch.zeros(2, 2)
ones_tensor = torch.ones(2, 2)

#float and integer tensors
float_tensor = torch.FloatTensor(data)
int_tensor = torch.IntTensor(data)
float_tensor=torch.tensor(data, dtype=torch.float32)

#device management
if torch.cuda.is_available():
    device = torch.device("cuda")
    tensor_on_gpu = tensor.to(device)

#arithmetic operations
tensor_a = torch.tensor([[1, 2], [3, 4]])
tensor_b = torch.tensor([[5, 6], [7, 8]])
#addition
added_tensor = tensor_a + tensor_b
#multiplication
multiplied_tensor = torch.matmul(tensor_a, tensor_b)

#indexing and slicing
first_row = tensor_a[0]
first_column = tensor_a[:, 0]
submatrix = tensor_a[0:2, 0:2]

#broadcasting
tensor_c = torch.tensor([[1], [2]])
broadcasted_tensor = tensor_a + tensor_c

#inplace operations
tensor_a.add_(tensor_b)


