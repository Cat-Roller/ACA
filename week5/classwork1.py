import numpy as np

#task 1
# Scenario: A retail chain has tracked the monthly spending of 60 customers over the last 6 months.

# Structure: 60 rows (Customers) x 6 columns (Months).

# np.random.seed(42) Spending ranges from 20 to
# 500 per month spending_data = np.random.randint(20, 501, (60, 6)) Task:

# Calculate the total spending for each customer over the 6-month period.

# Find the average monthly revenue for the store (average of all customers and all months).

# The "VIP" Filter: Identify how many customers spent more than $2,000 in total.

# Slicing Challenge: Calculate the total revenue for the last 3 months only.



# np.random.seed(42)
# spending_data = np.random.randint(20, 501, (60, 6)) 
# print(spending_data.shape)
# total_6m = np.sum(spending_data, axis=1)
# print(total_6m.shape)
# monthly_average = np.average(spending_data,axis=0)
# print(monthly_average)
# VIP_percentage = np.mean(total_6m>2000)
# print(VIP_percentage)
# three_month_data = spending_data[:,:3]
# print(three_month_data.shape)



# task2
# Scenario: You have a catalog of 100 products. You need to adjust their prices for 3 different international markets, each with a different "Inflation Adjustment Factor."

# Data:

# Python

# 100 base prices base_prices = np.random.uniform(5.0, 100.0, 100) Inflation factors for 3 countries inflation_factors = np.array([1.05, 1.12, 1.08]) Task:

# Use Broadcasting to create a 2D array of adjusted_prices with the shape (100, 3).

# Each column should represent the prices for one country (Base Price * Factor).

# Calculate the price difference (in dollars) between the most expensive country (Factor 1.12) and the cheapest country (Factor 1.05) for all 100 products.

# Find the maximum price difference found in the entire catalog.

base_prices = np.random.uniform(5.0, 100.0, 100)
inflation_factors = np.array([1.05, 1.12, 1.08])
inflated_prices = base_prices.reshape(100, 1) * inflation_factors.reshape(1, 3)
inflated_prices = np.multiply(base_prices,inflation_factors)
print(inflated_prices.shape)
price_diff = inflated_prices[:,1] - inflated_prices[:,0]
print(price_diff.shape)
print(max(price_diff))

# Problem 3: Quality Control & Batch Testing (Logic & Filtering)
# Scenario: You are testing the weight of 200 organic chocolate bars. The target weight is 100g.
# Data:Python 200 bars with slight variations weights = np.random.normal(100, 2, 200) 
# Task:Count how many bars are underweight (less than 98g).Count how many bars are overweight (more than 102g).
# Calculate the percentage of the batch that is considered "Perfect" (between 98g and 102g inclusive).
# Use a ufunc to calculate the total weight of the entire batch in Kilograms (kg).

# weights = np.random.normal(100, 2, 200)
# too_light = np.count_nonzero(weights<98)
# too_heavy = np.count_nonzero(weights>102)
# perfect_percentage = 100 - (too_light + too_heavy) / 2
# print(perfect_percentage)
# print(f'{np.add.reduce(weights)/1000:.2f}')