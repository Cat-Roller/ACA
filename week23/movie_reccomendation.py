import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
import implicit
from fuzzywuzzy import process

ratings_path = r"C:\Users\Aim\OneDrive\Рабочий стол\ACA\movie_reccomendation_data\combined_data_1.txt"
movies_path = r"C:\Users\Aim\OneDrive\Рабочий стол\ACA\movie_reccomendation_data\movie_titles.csv"

movies = []

with open(movies_path, "r", encoding="latin1") as f:
    for line in f:
        movie_id, year, title = line.strip().split(",", 2)
        movies.append([int(movie_id), year, title])

movies = pd.DataFrame(
    movies,
    columns=["movieId", "year", "title"]
)
ratings = []

with open(ratings_path, "r", encoding="latin1") as f:
    movie_id = None

    for line in f:
        line = line.strip()

        if line.endswith(":"):
            movie_id = int(line[:-1])
        else:
            user_id, rating, date = line.split(",")
            ratings.append([
                int(user_id),
                movie_id,
                int(rating),
                date
            ])

ratings =pd.DataFrame(
    ratings,
    columns=["userId", "movieId", "rating", "date"]
)

print(ratings.head())
print(movies.head())

def create_X(df):
    N = df["userId"].nunique()
    M = df["movieId"].nunique()

    user_mapper = dict(
        zip(
            np.unique(df["userId"]),
            list(range(N))
        )
    )

    movie_mapper =dict(
        zip(
            np.unique(df["movieId"]),
            list(range(M))
        )
    )

    user_inv_mapper = dict(
        zip(
            list(range(N)),
            np.unique(df["userId"])
        )
    )

    movie_inv_mapper = dict(
        zip(
            list(range(M)),
            np.unique(df["movieId"])
        )
    )

    user_index =[
        user_mapper[i]
        for i in df["userId"]
    ]

    movie_index = [
        movie_mapper[i]
        for i in df["movieId"]
    ]

    X = csr_matrix(
        (
            df["rating"],
            (movie_index, user_index)
        ),
        shape=(M, N)
    )

    return (
        X,
        user_mapper,
        movie_mapper,
        user_inv_mapper,
        movie_inv_mapper
    )

X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper = create_X(
    ratings
)

print(X.shape)

movie_title_mapper = dict(
    zip(
        movies["title"],
        movies["movieId"]
    )
)

movie_title_inv_mapper =dict(
    zip(
        movies["movieId"],
        movies["title"]
    )
)

def movie_finder(title):
    all_titles = movies["title"].tolist()
    closest_match = process.extractOne(
        title,
        all_titles
    )

    return closest_match[0]

def get_movie_index(title):
    fuzzy_title =movie_finder(title)

    movie_id =movie_title_mapper[fuzzy_title]

    movie_idx =movie_mapper[movie_id]

    return movie_idx

def get_movie_title(movie_idx):
    movie_id = movie_inv_mapper[movie_idx]

    title =movie_title_inv_mapper[movie_id]

    return title

model = implicit.als.AlternatingLeastSquares(
    factors=50
)

model.fit(X)

movie_of_interest = "The Matrix"

movie_index = get_movie_index(movie_of_interest)

related = model.similar_items(
    movie_index
)

print(f"Because you watched {movie_finder(movie_of_interest)}:")

for r in related:
    recommended_title = get_movie_title(r[0])

    if recommended_title != movie_finder(movie_of_interest):
        print(recommended_title)

user_id = 95

user_ratings = ratings[
    ratings["userId"] == user_id
].merge(
    movies[["movieId", "title"]],
    on="movieId"
)

user_ratings = user_ratings.sort_values(
    "rating",
    ascending=False
)

print(
    f"Number of movies rated by user {user_id}: "
    f"{user_ratings['movieId'].nunique()}"
)

print(user_ratings.head())

X_t = X.T.tocsr()

user_idx = user_mapper[user_id]

recommendations = model.recommend(
    user_idx,
    X_t
)

print(f"\nRecommendations for user {user_id}:")

for r in recommendations:
    recommended_title = get_movie_title(r[0])
    print(recommended_title)