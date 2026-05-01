import numpy as np
from sklearn.datasets import load_wine
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Load Data
data = load_wine()
X, y = data.data, data.target

# 2. Polynomial Features (degree = 2)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_poly, y, test_size=0.2, random_state=42
)

# 4. Parameter Grid
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5]
}

# 5. Model
rf = RandomForestClassifier(random_state=42)

# 6. GridSearch with 5-fold CV
grid = GridSearchCV(
    rf,
    param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid.fit(X_train, y_train)

# 7. Best parameters
print("Best Hyperparameters:", grid.best_params_)

# 8. Test set evaluation
best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)

test_accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", test_accuracy)

# 9. Compare CV score vs Test score
cv_score = grid.best_score_
print("Mean CV Accuracy:", cv_score)

if abs(cv_score - test_accuracy) > 0.05:
    print("Possible high variance (model may be overfitting).")
else:
    print("No strong signs of high variance.")