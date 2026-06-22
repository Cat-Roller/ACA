import tensorflow as tf
from keras.layers import Conv2D,Dropout,MaxPool2D,Dense,Flatten,ReLU
from keras.models import Sequential
import numpy as np
from torchvision import models,transforms
from torchvision.datasets import Caltech101
from torch.utils.data import DataLoader,random_split
from torch.nn import Linear


IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD  = [0.229, 0.224, 0.225]
root_path=r"C:\Users\Aim\OneDrive\Рабочий стол\ACA"

def get_transform(img_size):
    return transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD)
    ])

def load_dataset(root, img_size):
    transform = get_transform(img_size)
    dataset = Caltech101(root=root,download=False,transform=transform)

    return dataset

def build_loaders(root, img_size, batch_size=128, train_ratio = 0.8):
    dataset = load_dataset(root, img_size)

    train_size = int(train_ratio * len(dataset))
    val_size = len(dataset) - train_size

    train_set, val_set = random_split(dataset, [train_size, val_size])

    train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_set, batch_size=batch_size)

    return train_loader, val_loader

train_224, val_224 = build_loaders(root_path, 224)
train_299, val_299 = build_loaders(root_path, 299)

FCN = Sequential([
    Flatten(),
    Dense(1000),
    Dropout(0.4),
    ReLU(),
    Dense(500),
    Dropout(0.4),
    ReLU(),
    Dense(200),
    Dropout(0.4),
    ReLU(),
    Dense(101,activation='softmax')
])

LeNet = Sequential([
    Conv2D(10, kernel_size=(5,5), strides=(1,1),
          activation='relu', padding='valid',input_shape=(224,224,3)),
    MaxPool2D(pool_size=(2,2), strides=(2,2)),

    Conv2D(20, kernel_size=(5,5), strides=(1,1),
          activation='relu', padding='valid'),
    MaxPool2D(pool_size=(2,2), strides=(2,2)),

    Flatten(),

    Dense(400, activation='relu'),
    Dropout(0.2),

    Dense(200, activation='relu'),
    Dropout(0.2),

    Dense(101,activation='softmax')
    ])

AlexNet = models.AlexNet(weights='DEFAULT')

VGG_16 = models.vgg16(weights='DEFAULT')

ResNet_18 = models.resnet18(weights='DEFAULT')

Inception_v3 = models.inception_v3(weights='DEFAULT', aux_logits=False)

MobileNet_v2 = models.mobilenet_v2(weights="DEFAULT")

EfficientNet_b0 = models.efficientnet_b0(weights="DEFAULT")

AlexNet.classifier[6] = Linear(4096, 101)
VGG_16.classifier[6] = Linear(4096, 101)
ResNet_18.fc = Linear(ResNet_18.fc.in_features, 101)
Inception_v3.fc = Linear(Inception_v3.fc.in_features, 101)
MobileNet_v2.classifier[1] = Linear(MobileNet_v2.last_channel, 101)
EfficientNet_b0.classifier[1] = Linear(EfficientNet_b0.classifier[1].in_features,101)

