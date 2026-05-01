import numpy as np


#task1
prices = np.random.uniform(150, 200, 60)
prices[np.random.randint(0, 60, 10)] = np.nan
prices[np.isnan(prices)] = np.nanmean(prices)
print(np.log(prices))


#task2
# humidity = np.random.randint(0, 100, 100)
# danger_zone = humidity < 20
# print(danger_zone.sum())
# action_plan = np.where(danger_zone==0, 'Moniror', 'Activate sprinklers')
# print(np.average(humidity[humidity>=20]))

#task3
# humidity = np.random.randint(-5000, 60000, 50).astype(float)
# humidity[0>humidity] = np.nan
# humidity[humidity>30000] = np.nan
# print(np.nanmean(humidity))
# print(np.nansum(humidity))
# print(np.nanargmax(humidity))

#task4
# sales_data = np.random.uniform(5, 50, (2,60))
# print(np.sum(sales_data,axis=1))
# high_sales = (sales_data[0, :]>40) & (sales_data[1, :]>40)
# print(np.argmax(np.sum(sales_data, axis=0)))
# income_change = np.diff(sales_data[0,:])

#task5
# weights = np.random.uniform(1, 50, 80)
# distances = np.random.uniform(10, 1000, 80)

# cost = (weights * 0.5) + (distances *0.1)
# cost = np.where(distances > 500, cost + 20, cost)
# print(cost[cost > (cost.mean() + 1.5 * cost.std())])