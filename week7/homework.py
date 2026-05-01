import pandas as pd
import numpy as np
import seaborn as sns

spotify_data = pd.read_csv(r"C:\Users\Aim\.cache\kagglehub\datasets\yashdev01\spotify-tracks-dataset\versions\1\spotify-tracks-dataset.csv")

label_data = pd.DataFrame({
    'label_name': ['Sony Music', 'Universal Music', 'Warner Music', 'Independent'],
    'country_hq': ['USA', 'USA', 'USA', 'Global'],
    'prestige_score': [9.5, 9.8, 9.2, 8.0]
})

#task1
# love_song_popularity = spotify_data.loc[ spotify_data['track_name'].str.contains('love', False, na=False), 'popularity'].mean()
# print(love_song_popularity)


#task2
# spotify_data['main_artist'] = spotify_data['artists'].str.split(';').str[0]
# print(spotify_data['main_artist'].value_counts().head(1))

#task3
# spotify_data['is_remix'] = spotify_data['track_name'].str.contains('remix', case=False, na=False)
# remix_pivot = spotify_data.pivot_table(['danceability', 'energy'], 'is_remix', aggfunc='mean')
# print(remix_pivot.head())

#task4
# spotify_data['name_length'] = pd.cut(
#     spotify_data['track_name'].str.len(),
#     bins=[0, 15, 40, 1500],
#     labels=['Short', 'Medium', 'Long'],
# )

# length_popularity = spotify_data.pivot_table('popularity','name_length')
# print(length_popularity)

#task5
spotify_data['is_acoustic'] = spotify_data['track_name'].str.contains('acoustic', case=False, na=False) | (spotify_data['track_genre'] == 'acoustic')
spotify_data['label_assignment'] = np.where(
    spotify_data['is_acoustic'],
    'Independent',
    'Universal Music'
)

merged_df: pd.DataFrame = spotify_data.merge(
    label_data,
    left_on='label_assignment',
    right_on='label_name')

print(merged_df.head())
stat_pivot = merged_df.pivot_table(
    index='is_acoustic',
    values=['track_name', 'prestige_score'],
    aggfunc={
        'track_name': 'count',
        'prestige_score': 'mean'
    })
print(stat_pivot)