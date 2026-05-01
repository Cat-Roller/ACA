from matplotlib.patches import ArrowStyle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- DATA SETUP ---
df = pd.read_csv("countries_data.csv")

# ==========================================
# TASK 1 (NumPy): Percentiles
# English: Use NumPy to calculate the 10th percentile of 'Infant mortality (per 1000 births)'.
# Հայերեն: Օգտագործեք NumPy-ը՝ հաշվելու 'Infant mortality (per 1000 births)'-ի 10-րդ պերցենտիլը:
# ------------------------------------------

# percent_10 = np.nanpercentile(df['Infant mortality (per 1000 births)'],10)
# print(percent_10)

# ==========================================
# TASK 2 (NumPy): Conditional Labeling
# English: Create a new column 'Birth_Category' using np.where. 
# If 'Birthrate' > 30, label it 'High', otherwise 'Normal'.
# Հայերեն: Ստեղծեք նոր 'Birth_Category' սյունակ՝ օգտագործելով np.where: 
# Եթե 'Birthrate' > 30, նշեք 'High', հակառակ դեպքում՝ 'Normal':
# ------------------------------------------

# df['Birth_category'] = np.where(df['Birthrate']>30,'High','Normal')
# print(df['Birthrate'].iloc[:5], df['Birth_category'].iloc[:5],sep='\n')

# ==========================================
# TASK 3 (Pandas): Multi-Condition Filtering
# English: Filter for countries in 'SUB-SAHARAN AFRICA' with 'Phones (per 1000)' > 100.
# Հայերեն: Զտեք այն երկրները 'SUB-SAHARAN AFRICA' տարածաշրջանում, որոնք ունեն 100-ից ավել 'Phones (per 1000)':
# ------------------------------------------

# ans_3 = df[(df['Region'] == 'SUB-SAHARAN AFRICA') & (df['Phones (per 1000)'] > 100)]
# print(ans_3)

# ==========================================
# TASK 4 (Pandas): Grouped Aggregation
# English: Group by 'Region' and calculate the mean 'Service' (economic sector) for each region.
# Հայերեն: Խմբավորեք ըստ 'Region'-ի և հաշվեք յուրաքանչյուր տարածաշրջանի 'Service' (տնտեսական ոլորտ) միջինը:
# ------------------------------------------

# service_rate_per_region = df.groupby('Region')['Service'].mean()
# print(service_rate_per_region)

# ==========================================
# TASK 5 (Matplotlib): Visualization & Annotation
# English: Create a scatter plot of 'Area (sq. mi.)' vs 'Population'.
# 1. Use log scales for both axes (plt.xscale('log'), plt.yscale('log')).
# 2. Color points by 'GDP ($ per capita)'.
# 3. Use plt.annotate to label 'China'.
# Հայերեն: Ստեղծեք 'Area (sq. mi.)'-ի և 'Population'-ի scatter plot:
# 1. Օգտագործեք լոգարիթմական սանդղակներ երկու առանցքների համար:
# 2. Գունավորեք կետերը ըստ 'GDP ($ per capita)'-ի:
# 3. Օգտագործեք plt.annotate՝ «China»-ն պիտակավորելու համար:
# ------------------------------------------

plt.scatter(df['Area (sq. mi.)'], df['Population'], c=df['GDP ($ per capita)'], cmap='viridis')
plt.colorbar(label='GDP ($ per capita)')
x = df['Area (sq. mi.)'].max()
y = df['Population'].max()
plt.annotate('China',
             (x,y),
             xytext = (20, 20),
             textcoords="offset points",
             arrowprops = dict(arrowstyle = "->", color = 'red')
             )
plt.xscale('log')
plt.yscale('log')


plt.xlabel('Area (sq. mi.)')
plt.ylabel('Population')
plt.title('Area vs Population')
plt.show()