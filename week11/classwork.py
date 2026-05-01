import pandas as pd
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from hyperopt

df = pd.read_csv(r"movie_classification.csv")

df["3D_available"] = df["3D_available"].map({"YES": 1, "NO": 0})
df["Genre"] = df["Genre"].astype("category")

X = df.drop("Start_Tech_Oscar", axis=1)
y = df["Start_Tech_Oscar"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

cat_features = X.select_dtypes(include=["category"]).columns.tolist()

model = CatBoostClassifier(
    iterations=200,
    depth=5,
    learning_rate=0.1,
    loss_function="Logloss",
    eval_metric="F1",
    random_seed=42,
    verbose=0
)

model.fit(X_train, y_train, cat_features=cat_features)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))