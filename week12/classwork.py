import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv(r'C:\Users\Aim\OneDrive\Рабочий стол\ACA\week12\mall_customers.csv')

X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

WCSS = []

for i in range(1, 12):
    model = KMeans(n_clusters=i)
    model.fit(X)
    WCSS.append(model.inertia_)

plt.plot(range(1, 12), WCSS)
plt.xlabel("number of clusters")
plt.ylabel("WCSS")
plt.show()