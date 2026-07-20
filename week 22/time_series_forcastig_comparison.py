import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pmdarima.arima import ARIMA
import xgboost as xgb
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_percentage_error 

df = pd.read_csv(r"C:\Users\Aim\OneDrive\Рабочий стол\ACA\week 22\stock_data.csv",
                 parse_dates=True,
                 index_col="Date",
                 usecols=['Date','Close'])
df.dropna(inplace =True)
df.head()

train = df[:-90]
test = df[-90:]

arima_train = np.log(train['Close'])

arima = ARIMA(
    order=(4, 2, 1),
    seasonal_order=(1, 0, 2, 5),
    with_intercept=True
)

arima.fit(arima_train)
#arima returns NaN bug
arima.summary()
forecast = arima.predict(n_periods=90)

xgb_train = train.copy()

for i in range(1, 31):
    xgb_train[f'Close_lag_{i}'] = df['Close'].shift(i)

xgb_train.dropna(inplace=True)
xgb_train_x = xgb_train.drop(columns='Close')
xgb_train_y = xgb_train['Close']

xgb_model = xgb.XGBRegressor(
    n_estimators = 500,
    learning_rate = 0.025,
    max_depth = 7,
    objective = 'reg:squarederror',
    suppress_warnings=True
)

xgb_model.fit(xgb_train_x,xgb_train_y)

history = list(xgb_train["Close"])
predictions = []

for _ in range(90):
    X_input = np.array(history[-30:]).reshape(1, -1)

    prediction = xgb_model.predict(X_input)[0]

    predictions.append(prediction)
    history.append(prediction)

exponential_model = ExponentialSmoothing(
    train,
    trend="add",
    seasonal="add",
    seasonal_periods=5
)

exponential_model = exponential_model.fit()

arima_predictions = np.exp(forecast)
arima_predictions = pd.Series(
    arima_predictions,
    index=test.index
)
xgb_predictions = pd.Series(
    predictions,
    index=test.index
)
exponential_predictions = exponential_model.forecast(90)

arima_mape = mean_absolute_percentage_error(
    test["Close"],
    arima_predictions
)

xgb_mape = mean_absolute_percentage_error(
    test["Close"],
    xgb_predictions
)

exponential_mape = mean_absolute_percentage_error(
    test["Close"],
    exponential_predictions
)

mape_results = pd.DataFrame({
    "Model": [
        "Auto ARIMA",
        "XGBoost",
        "Exponential Smoothing"
    ],
    "MAPE": [
        arima_mape,
        xgb_mape,
        exponential_mape
    ]
})

print(mape_results)

mape_results["MAPE (%)"] = mape_results["MAPE"] * 100

print(mape_results[["Model", "MAPE (%)"]])

plt.figure(figsize=(15, 8))

plt.plot(
    test.index,
    test["Close"],
    label="Actual Close"
)

plt.plot(
    test.index,
    arima_predictions,
    label=f"Auto ARIMA (MAPE: {arima_mape * 100:.2f}%)"
)

plt.plot(
    test.index,
    xgb_predictions,
    label=f"XGBoost (MAPE: {xgb_mape * 100:.2f}%)"
)

plt.plot(
    test.index,
    exponential_predictions,
    label=f"Exponential Smoothing (MAPE: {exponential_mape * 100:.2f}%)"
)

plt.title("90-Day Stock Price Forecast Comparison")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.grid(True)
plt.show()