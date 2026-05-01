#task1
# import numpy as np

# data = np.random.randint(20, 45, (4, 5, 2))
# print(data)
# print(data.mean(axis=(1,2)))
# print(data.max(axis=(0)))
# print(data.var(axis=1).mean(axis=0))

# task2
# data = np.random.randint(100, 1000, (10,3))
# print(data)
# normalized_data = (data - np.mean(data,axis=1,keepdims=True)) / np.std(data,axis=1,keepdims=True)
# print(normalized_data)
# print(np.mean(normalized_data,axis=1))
# print(np.std(normalized_data,axis=1))

#task3
# coords = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
# coords[:, 0]+=3
# coords[:, 1]+=5
# print(coords)
# coords = np.multiply(coords,2.5)
# print(coords)
# distances = coords[:,0]**2 + coords[:,1]**2
# print(distances)

#task4
# rods = np.array([10.1, 9.8, 10.5, 10.0, 9.9, 10.2, 11.0, 9.0, 10.1, 10.0])
# mean = rods.mean()
# std = rods.std()
# defective = (rods >= mean - 2*std) & (rods <= mean + 2*std)
# print(np.sum(defective)/len(defective)*100,'%')

#task5
# grades = np.array([85, 92, 78, 88, 95])

# weights = np.array([3, 4, 3, 2, 5])

# weighted_avg = np.sum(grades * weights) / np.sum(weights)
# print(weighted_avg)

# grades[grades<90] += 5

# bonus_weighted_avg = np.sum(grades * weights) / np.sum(weights)
# print(bonus_weighted_avg)