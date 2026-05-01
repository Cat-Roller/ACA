import yfinance as yf
import pandas as pd
import numpy as np

msft = pd.read_csv("msft.csv", parse_dates=["Date"], index_col="Date")
print(msft.head())

#task1
monthly_avg_close = msft["Close"].resample("M").mean()

# Month with highest average close
max_month = monthly_avg_close.idxmax()
max_value = monthly_avg_close.max()

print("Highest avg close month:", max_month.strftime("%Y-%m"))
print("Average close:", round(max_value, 2))