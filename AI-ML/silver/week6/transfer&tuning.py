import torchvision.models as models
from transformers import BertTokenizer, BertModel

resnet=models.resnet18(pretrained=True)
model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

for param in resnet.parameters():
    param.requires_grad = False

#replace the final fully connected layer with a new one for our specific task
resnet.fc = torch.nn.Linear(resnet.fc.in_features, 10)  # assuming we have 10 classes

