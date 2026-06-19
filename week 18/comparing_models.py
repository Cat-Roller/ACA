import tensorflow as tf
import tensorflow_datasets as tfds
from keras.layers import Conv2D,Dropout,MaxPool2D,Dense,Flatten,ReLU
from keras.models import Sequential
import numpy as np
from torchvision import models

IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD  = [0.229, 0.224, 0.225]

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

AlexNet = models.AlexNet(num_classes=101,pretrained=True)

VGG_16 = models.vgg16(weights='DEFAULT')

ResNet_18 = models.resnet18(weights='DEFAULT')

Inception_v3 = models.inception_v3(weights='DEFAULT', aux_logits=False)

MobileNet_v2 = models.mobilenet_v2(weights="DEFAULT")

EfficientNet_b0 = models.efficientnet_b0(weights="DEFAULT")

def preprocess(image, label):
    image = tf.image.resize(image, (224, 224))

    image = tf.cast(image, tf.float32) / 255.0

    image = (image - IMAGENET_MEAN) / IMAGENET_STD
    return image, label

def preprocess_299(image, label):
    image = tf.image.resize(image, (299, 299))

    image = tf.cast(image, tf.float32) / 255.0

    image = (image - IMAGENET_MEAN) / IMAGENET_STD
    return image, label