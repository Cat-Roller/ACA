import pandas as pd
from sklearn.datasets import load_breast_cancer, load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

# raw_cancer_data = load_breast_cancer()

# cancer_data = pd.DataFrame(data=raw_cancer_data.data, columns=raw_cancer_data.feature_names  )
# cancer_data['target'] = raw_cancer_data.target 
# print(cancer_data.head())

# x_train,x_test,y_train,y_test = train_test_split(raw_cancer_data.data,raw_cancer_data.target,random_state=30)

# dt = DecisionTreeClassifier()
# rf = RandomForestClassifier(n_estimators=100)
# xgb = XGBClassifier()

# dt.fit(x_train, y_train)
# rf.fit(x_train, y_train)
# xgb.fit(x_train, y_train)

# dt_acc = accuracy_score(y_test, dt.predict(x_test))
# rf_acc = accuracy_score(y_test, rf.predict(x_test))
# xgb_acc = accuracy_score(y_test, xgb.predict(x_test))

# print(dt_acc)
# print(rf_acc)
# print(xgb_acc)



#task2
data = load_wine()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y)

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5]
}

rf = RandomForestClassifier(random_state=10)

grid = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    return_train_score=True
)

grid.fit(X_train, y_train)
best_model = grid.best_estimator_

print("Best Parameters:", grid.best_params_)

y_pred = best_model.predict(X_test)

test_accuracy = accuracy_score(y_test, y_pred)
cv_accuracy = grid.best_score_
train_accuracy = best_model.score(X_train, y_train)

print("Cross-Validation Accuracy:", cv_accuracy)
print("Training Accuracy:", train_accuracy)
print("Test Accuracy:", test_accuracy)