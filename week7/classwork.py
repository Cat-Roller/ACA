import pandas as pd
import numpy as np
import seaborn as sns
import ssl

spotify_data = pd.read_csv(r"C:\Users\Aim\.cache\kagglehub\datasets\yashdev01\spotify-tracks-dataset\versions\1\spotify-tracks-dataset.csv")

# hits = spotify_data[
#     (spotify_data['popularity'] > 80) &
#     (spotify_data['track_genre'].isin(['pop', 'rock']))
# ].sort_values(by='popularity', ascending=False)
# print(hits)

# energy_levels = spotify_data.pivot_table(
#     index='track_genre',
#     values='energy',
#     aggfunc='mean'
#     ).sort_values(by='energy', ascending=False)
# print(energy_levels.iloc[0])

# spotify_data['vibe_score'] = (spotify_data['danceability'] + spotify_data['valence']) * spotify_data['energy']
# vibe_check = spotify_data.loc[
#     (spotify_data['explicit']) & (spotify_data['vibe_score'] > 1.5),
#     ['track_name', 'artists', 'vibe_score']
# ]
# print(vibe_check)


# musician_data = spotify_data.pivot_table(index='key', values='popularity', margins=True, columns='mode', aggfunc='mean')
# print(musician_data)

artist_metadata = pd.DataFrame({
    'artist_name': ['Taylor Swift', 'Drake', 'Bad Bunny', 'BTS', 'Arctic Monkeys'],
    'global_region': ['North America', 'North America', 'Latin America', 'Asia', 'Europe'],
    'is_independent': [False, False, False, False, True]
})

df_merged = spotify_data.merge(
    artist_metadata,
    left_on='artists',
    right_on='artist_name',
    how='left'
)

independent_artists = df_merged[df_merged['is_independent'].fillna(False)]
independent_artists = independent_artists[independent_artists['is_independent']]
independent_artists = independent_artists[independent_artists['is_independent'].eq(True, fill_value=False)]
independent_artists = independent_artists.drop('is_independent')

global_data = independent_artists.pivot_table(
    index='global_region',
    values='track_name',
    aggfunc={'track_name':'count', 'tempo':'mean'},
)
print(global_data)