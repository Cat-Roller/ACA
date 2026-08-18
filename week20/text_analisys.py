import torch
import torch.nn as nn
import torch.optim as optim

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

#gotta fix the data
df = pd.read_csv(r'C:\Users\Aim\.cache\kagglehub\datasets\jrobischon\wikipedia-movie-plots\versions\1\wiki_movie_plots_deduped.csv')

df = df.dropna(subset=["Plot", "Genre"])

X = df["Plot"].values
y = df["Genre"].values
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

vectorizer = TfidfVectorizer(max_features=20000, stop_words="english")

X_train = vectorizer.fit_transform(X_train).toarray()
X_test = vectorizer.transform(X_test).toarray()

X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)

y_train = torch.tensor(y_train, dtype=torch.long)
y_test = torch.tensor(y_test, dtype=torch.long)

class DNN(nn.Module):
    def __init__(self, input_dim, num_classes):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Dropout(0.5),

            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.5),

            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        return self.net(x)
    
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = DNN(X_train.shape[1], len(label_encoder.classes_)).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

epochs = 5

for epoch in range(epochs):
    model.train()

    optimizer.zero_grad()

    outputs = model(X_train.to(device))
    loss = criterion(outputs, y_train.to(device))

    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

model.eval()

with torch.no_grad():
    outputs = model(X_test.to(device))
    preds = torch.argmax(outputs, dim=1).cpu()

    accuracy = (preds == y_test).float().mean()

print("Test Accuracy:", accuracy.item())