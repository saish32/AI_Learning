from torchvision.transforms import AdjustBrightness, AdjustContrast, ColorJitter, RandomCrop, ToTensor, RandomHorizontalFlip, RandomRotation, Normalize, Compose, Resize
from nltk.tokenize import word_tokenize
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import torch.nn as nn

transform = RandomCrop(size=(224, 224))

transform = RandomHorizontalFlip(p=0.5)

transform = RandomRotation(degrees=15)

transform = ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1)

transform = AdjustBrightness(brightness_factor=0.2)

transform = AdjustContrast(contrast_factor=0.2)

tokens = word_tokenize("This is a sample sentence for tokenization.")

tokens = list("this is a sample sentence for tokenization.")

padded_sequences = pad_sequences([[1, 2, 3], [4, 5]], maxlen=5, padding='post')

truncated_sequences = pad_sequences([[1, 2, 3], [4, 5]], maxlen=2, truncating='post')

rnn=nn.LSTM(input_size=10, hidden_size=20, num_layers=2, batch_first=True)

data['rolling_mean'] = data['value'].rolling(window=3).mean()


