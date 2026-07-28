import pandas as pd
import numpy as np
import xgboost as xgb
import lightgbm as lgb
import pmdarima as pm
from prophet import Prophet
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_percentage_error 



data = pd.read_csv(r"C:\Users\Aim\.cache\kagglehub\datasets\tanayatipre\store-sales-forecasting-dataset\versions\1\stores_sales_forecasting.csv",encoding='latin1')

data["Order Date"] = pd.to_datetime(data["Order Date"])
monthly_sales = (
    data.groupby(pd.Grouper(key="Order Date", freq="MS"))["Sales"]
      .sum()
      .reset_index()
)

train = monthly_sales[:-12].copy()
test = monthly_sales[-12:].copy()

lag_sales = monthly_sales.copy()

for i in range(1,13):
    lag_sales[f'lag_{i}'] = lag_sales['Sales'].shift(i)

lag_sales.dropna(inplace = True)
train_lag = lag_sales[:-12]
test_lag = lag_sales[-12:]

X_train = train_lag.drop(columns=["Order Date", "Sales"])
y_train = train_lag["Sales"]

X_test = test_lag.drop(columns=["Order Date", "Sales"])

lgb_model = lgb.LGBMRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    random_state=42,
    verbosity=-1
)

lgb_model.fit(X_train, y_train)

lgb_predictions = lgb_model.predict(X_test)

xgb_model = xgb.XGBRegressor(
    objective="reg:squarederror",
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    random_state=42
)

xgb_model.fit(X_train, y_train)

xgb_predictions = xgb_model.predict(X_test)

arima_model = pm.auto_arima(
    train["Sales"],
    seasonal=True,
    start_p=0,
    start_q=0,
    max_p=10,
    max_d=10,
    m=12,
    trace=True,
    suppress_warnings=True
)

arima_predictions = arima_model.predict(n_periods=12)

exp_model = ExponentialSmoothing(
    train['Sales'],
    trend='add',
    seasonal='add',
    seasonal_periods=12
).fit()

exp_predictions = exp_model.forecast(12)

prophet_train = train.rename(columns = {'Order Date' : 'ds', 'Sales' : 'y'})

prophet = Prophet(
    yearly_seasonality=True,
    )
prophet.fit(prophet_train)

future = prophet.make_future_dataframe(
    periods=12,
    freq="MS"
)

forecast = prophet.predict(future)

prophet_predictions = forecast["yhat"].tail(12).values

lgb_mape = mean_absolute_percentage_error(
    test['Sales'],
    lgb_predictions
)

xgb_mape = mean_absolute_percentage_error(
    test["Sales"],
    xgb_predictions
)

arima_mape = mean_absolute_percentage_error(
    test["Sales"],
    arima_predictions
)


exponential_mape = mean_absolute_percentage_error(
    test["Sales"],
    exp_predictions
)

prophet_mape = mean_absolute_percentage_error(
    test['Sales'],
    prophet_predictions
)

mape_results = pd.DataFrame({
    "Model": [
        "LightGBM",
        "XGBoost",
        "Auto ARIMA",
        "Exponential Smoothing",
        "Prophet"
    ],
    "MAPE": [
        lgb_mape,
        xgb_mape,
        arima_mape,
        exponential_mape,
        prophet_mape
    ]
})

print(mape_results)

mape_results["MAPE (%)"] = mape_results["MAPE"] * 100

print(mape_results[["Model", "MAPE (%)"]])
