import pandas as pd
import numpy as np

msft = pd.read_csv("msft.csv", parse_dates=["Date"], index_col="Date")
print(msft.head())

#task3
# msft['year_ago_close'] = msft['Close'].shift(252)
# msft['yearly_change'] = msft['Close'] - msft['year_ago_close']
# msft.dropna(inplace=True)
# print(msft.head())

#task4
# msft = msft.asfreq('H', method='ffill')

#task5
# msft['quarter_close'] = msft['Close'].asfreq('Q')
# msft.dropna(inplace=True)
# msft['quarterly_change'] = (msft['quarter_close'] - msft['quarter_close'].shift(1)) / msft['quarter_close']
# msft['quarterly_moving_average'] = msft['quarter_close'].rolling(4).mean()
# msft.dropna(inplace=True)

#task6
# msft['change_percent'] = (msft['Close'] - msft['Close'].shift(1)) / msft['Close']
# msft.dropna(inplace=True)
# weekly_volatility = msft['change_percent'].resample('W').std()
# volatile_weeks = weekly_volatility[weekly_volatility <= (2*weekly_volatility.shift(1))]
# print(volatile_weeks)

#task7
# msft['50day_moving_average'] = msft['Close'].rolling(50).mean()
# msft['200day_moving_average'] = msft['Close'].rolling(200).mean()
# msft.dropna(inplace=True)
# buy_days = msft[
#     (msft['200day_moving_average']<msft['50day_moving_average'] )
#     & (msft['200day_moving_average'].shift(1)>msft['50day_moving_average'].shift(1))]
# print(buy_days)

#task8
weekend_change =(msft[msft.index.dayofweek == 4].shift(1)['Close']) - (msft[msft.index.dayofweek == 4]['Close'])
weekend_change = weekend_change.bfill()

print(weekend_change)