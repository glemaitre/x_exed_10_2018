popular_movie_id = data.groupby('movie_id')['rating'].mean().nlargest(10).index.values
movies.set_index('movie_id').loc[popular_movie_id]['title']