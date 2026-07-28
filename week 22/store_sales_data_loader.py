import kagglehub
import os
import pandas as pd
# Download latest version
path = kagglehub.dataset_download("tanayatipre/store-sales-forecasting-dataset")

print("Path to dataset files:", path)
df = pd.read_csv(path + '/' + os.listdir(path)[0], encoding='latin1')
print(df.head(5))
