import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import re
from sklearn.ensemble import VotingClassifier

data = pd.read_csv(r"C:\Users\Aim\.cache\kagglehub\datasets\team-ai\spam-text-message-classification\versions\1\SPAM text message 20170820 - Data.csv")

data["Category"] = data["Category"].map({"ham": 0, "spam": 1})

x = data['Message']
y = data['Category']

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

print("Engineering linguistic features...")
features = data['Message'].apply(linguistic_features)
data = pd.concat([data, features], axis=1)

print(data.head(3))

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

transformer = TfidfVectorizer(stop_words='english')

X_train_tfidf = transformer.fit_transform(X_train).todense()
X_test_tfidf  = transformer.transform(X_test)

model = MultinomialNB()
mnb = MultinomialNB()

model.fit(X_train_tfidf,y_train)

model_predictions = model.predict(X_test_tfidf)

print('Accuracy: ',accuracy_score(y_test,model_predictions))
print('Classification report: ')
print(classification_report(y_test,model_predictions))
print("Confusion matrix: ")
print(confusion_matrix(y_test,model_predictions))

model = LogisticRegression()
lr = LogisticRegression()

model.fit(X_train_tfidf,y_train)

model_predictions = model.predict(X_test_tfidf)

print('Accuracy: ',accuracy_score(y_test,model_predictions))
print("Confusion matrix: ")
print(confusion_matrix(y_test,model_predictions))

model = RandomForestClassifier()
rf = RandomForestClassifier()

model.fit(X_train_tfidf,y_train)

model_predictions = model.predict(X_test_tfidf)

print('Accuracy: ',accuracy_score(y_test,model_predictions))
print("Confusion matrix: ")
print(confusion_matrix(y_test,model_predictions))

ensemble = VotingClassifier(estimators=[('mnb',mnb),('lr',lr),('rf',rf)], voting='soft')
ensemble.fit(X_train_tfidf,y_train)

ensemble_votes = ensemble.predict(X_test_tfidf)

print('Accuracy: ',accuracy_score(y_test,ensemble_votes))
print('Classification report: ')
print(classification_report(y_test,ensemble_votes))
print("Confusion matrix: ")
print(confusion_matrix(y_test,ensemble_votes))
