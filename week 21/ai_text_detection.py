import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt


COMMON_STOPS = set('the a an and or but if then this that these those is are was were be been being '
                   'have has had do does did will would could should may might must can shall '
                   'i you he she it we they me him her us them my your his its our their '
                   'in on at to for of with by from as into about over under after before'.split())

def linguistic_features(text):
    text = str(text)
    words      = text.split()
    sentences  = re.split(r'[.!?]+', text)
    sentences  = [s for s in sentences if s.strip()]
    n_words    = max(len(words), 1)
    n_chars    = max(len(text), 1)
    word_lens  = [len(w) for w in words]
    lower_words = [w.lower().strip('.,!?;:') for w in words]
    unique     = len(set(lower_words))
    stops      = sum(1 for w in lower_words if w in COMMON_STOPS)
    upper      = sum(1 for c in text if c.isupper())
    digits     = sum(1 for c in text if c.isdigit())
    cap_words  = sum(1 for w in words if w and w[0].isupper())

    return pd.Series({
        'char_count':       len(text),
        'sentence_count':   max(len(sentences), 1),
        'avg_word_length':  np.mean(word_lens) if word_lens else 0,
        'lexical_diversity': unique / n_words,
        'punct_density':    sum(1 for c in text if c in '.,!?;:') / n_chars,
        'comma_density':    text.count(',') / n_chars,
        'question_density': text.count('?') / n_chars,
        'uppercase_ratio':  upper / n_chars,
        'stopword_ratio':   stops / n_words,
        'digit_ratio':      digits / n_chars,
        'cap_word_ratio':   cap_words / n_words,
        'long_word_ratio':  sum(1 for w in words if len(w) > 6) / n_words,
    })


data = pd.read_csv(r'C:\Users\Aim\.cache\kagglehub\datasets\alitaqishah\ai-vs-human-text-classification-dataset-2026\versions\1\ai_vs_human_text_2026.csv')
data['label'] = data['label'].map({'human': 0, 'ai':1})

X = data['text_content'].apply(linguistic_features)
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = CatBoostClassifier(
    iterations=500,
    learning_rate=0.05,
    depth=6,
    loss_function='Logloss',
    eval_metric='Accuracy',
    verbose=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)


y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()