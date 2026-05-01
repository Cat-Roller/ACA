import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv(r'C:\Users\Aim\OneDrive\Рабочий стол\ACA\week12\mall_customers.csv')

x = df[["Annual Income (k$)", "Spending Score (1-100)"]]

model = KMeans(n_clusters=5)
df["cluster"] = model.fit_predict(x)

plt.figure()
plt.scatter(x["Annual Income (k$)"], x["Spending Score (1-100)"], c=df["cluster"])
plt.xlabel("annual income (k$)")
plt.ylabel("spending score (1-100)")
plt.title("customer clusters")
plt.show()