from keras.datasets import cifar10
from keras.layers import Conv2D,Dropout,MaxPool2D,Dense,Flatten
from keras.models import Sequential

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

model = Sequential([
    Conv2D(10, kernel_size=(5,5), strides=(1,1),
          activation='relu', padding='valid',input_shape=(32,32,3)),
    MaxPool2D(pool_size=(2,2), strides=(2,2)),

    Conv2D(20, kernel_size=(5,5), strides=(1,1),
          activation='relu', padding='valid'),
    MaxPool2D(pool_size=(2,2), strides=(2,2)),

    Flatten(),

    Dense(400, activation='relu'),
    Dropout(0.2),

    Dense(120, activation='relu'),
    Dropout(0.2),

    Dense(84, activation='relu'),
    Dropout(0.2),

    Dense(10,activation='softmax')
    ])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


history = model.fit(
    x_train, y_train,
    epochs=20, batch_size=64,
    validation_split=0.1, shuffle=True
)

test_loss, test_acc = model.evaluate(x_test, y_test)

print(f"Test accuracy: {test_acc}")