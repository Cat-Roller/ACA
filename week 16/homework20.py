#download data
# import kagglehub

# path = kagglehub.dataset_download("stefanoleone992/fifa-22-complete-player-dataset")

# print("Path to dataset files:", path)

#filtering data
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt



players = pd.read_csv(r'C:\Users\Aim\.cache\kagglehub\datasets\stefanoleone992\fifa-22-complete-player-dataset\versions\3\players_22.csv')
print(players.shape)
players = players[players['club_position'] != 'GK']
print(players.shape)

features = ['overall','potential','age','height_cm','weight_kg','pace','shooting','passing','dribbling','defending','physic',
            'attacking_crossing','attacking_finishing','attacking_heading_accuracy','attacking_short_passing','attacking_volleys','skill_dribbling',
            'skill_curve','skill_fk_accuracy','skill_long_passing','skill_ball_control']
players = players[features]

print(f'there are {players.isnull().any(axis=1).sum()} rows containing null values')

players = players.fillna(players.mean())
players = pd.DataFrame(StandardScaler().fit_transform(players), columns=players.columns)

print(players.head())

#pca analyses
pca_80_percent = PCA(n_components=0.8)
players_pca = pca_80_percent.fit_transform(players)
pca_2_variables = PCA(n_components=2)
player_two_components = pca_2_variables.fit_transform(players)

print(f"number of components to remain 80% variance is {pca_80_percent.n_components_}")
    
pc1 = players_pca[:,0]
pc2 = players_pca[:,1]

loadings = pd.DataFrame(
    pca_2_variables.components_.T,
    columns=["pc1", "pc2"],
    index=features
)

print(loadings.sort_values(by="pc1", ascending=False))
print(loadings.sort_values(by="pc2", ascending=False))

plt.figure()
plt.scatter(pc1,pc2, c=players["overall"], cmap="viridis")
plt.xlabel("ball controll")
plt.ylabel("talent")
plt.title("player pca space colored by overall rating")
plt.colorbar(label="overall rating")
plt.show()