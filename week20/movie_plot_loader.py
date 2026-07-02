import pandas as pd
import kagglehub
import os

print("Downloading Wikipedia Movie Plots...")
movie_folder_path = kagglehub.dataset_download("jrobischon/wikipedia-movie-plots")

movie_file_path = os.path.join(movie_folder_path, "wiki_movie_plots_deduped.csv")
df_movies = pd.read_csv(movie_file_path)

print(f"Success! Loaded {len(df_movies)} movie records.")
print(df_movies[['Title', 'Genre']].head(3), "\n")
print(movie_file_path)