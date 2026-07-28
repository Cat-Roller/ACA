import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv(r"C:\Users\Aim\.cache\kagglehub\datasets\tanayatipre\store-sales-forecasting-dataset\versions\1\stores_sales_forecasting.csv",encoding='latin1')

print(data.head())
print(data.info())
print(data.describe())

data["Order Date"] = pd.to_datetime(data["Order Date"])
monthly_sales = (
    data.groupby(pd.Grouper(key="Order Date", freq="MS"))["Sales"]
      .sum()
      .reset_index()
)

print(monthly_sales.head())

sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Order Date', y='Sales', label='Revenue', color='blue')

plt.xlabel('Date')
plt.ylabel('Revenue')
plt.title('Revenue Price Over Time')

plt.show()