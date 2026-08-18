import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments
from sklearn.model_selection import train_test_split

path = r'C:\Users\Aim\.cache\kagglehub\datasets\lakshmi25npathi\imdb-dataset-of-50k-movie-reviews\versions\1\IMDB Dataset.csv'

data = pd.read_csv(path)

data['sentiment'] = data['sentiment'].map({'positive':1, 'negative':0})

print(data.head(4))

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
X = data['review'].apply(tokenizer)
y = data['sentiment']
print(50*'=')
print(X.head(4))
print(50*'=')

model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=2
)
