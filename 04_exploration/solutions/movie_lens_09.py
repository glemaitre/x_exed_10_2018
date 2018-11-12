most_voted_movie_id = df.sort_values('count', ascending=False).reset_index().loc[0, 'movie_id']
movies.set_index('movie_id').loc[most_voted_movie_id]