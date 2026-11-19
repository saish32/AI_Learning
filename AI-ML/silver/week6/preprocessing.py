from lightgbm import Dataset
import torchvision.datasets as datasets
from torchvision.transforms import ToTensor
from torchvision.transforms import Normalize, Compose, Resize, RandomHorizontalFlip, RandomRotation
import os
from PIL import Image
from torch.utils.data import DataLoader

#load the MNIST dataset
mnist_train = datasets.MNIST(root='data', train=True, download=True, transform=ToTensor())
mnist_test = datasets.MNIST(root='data', train=False, download=True, transform=ToTensor())

#custom dataset class
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, data, labels, transform=None):
        self.data = data
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx]
        label = self.labels[idx]

        if self.transform:
            sample = self.transform(sample)

        return sample, label

#normalization transform

transform = Normalize(mean=[0.5], std=[0.5])
transform = Compose([Resize((28, 28)), ToTensor(), transform])

transform=Compose([RandomHorizontalFlip(), RandomRotation(10), ToTensor(), Normalize(mean=[0.5], std=[0.5])])

#custom dataset with transformations
class CustomImageDataset(Dataset):
    def __init__(self, image_dir, transform=None):
        self.image_dir = image_dir
        self.transform = transform
        self.image_files = [f for f in os.listdir(image_dir) if f.endswith('.png') or f.endswith('.jpg')]

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_path = os.path.join(self.image_dir, self.image_files[idx])
        image = Image.open(img_path).convert("RGB")
        
        if self.transform:
            image = self.transform(image)
        
        return image

#create a DataLoader for the custom dataset
image_dataset = CustomImageDataset(image_dir='path/to/images', transform=transform)
image_dataloader = DataLoader(image_dataset, batch_size=32, shuffle=True, num_workers=4)




 