df = data.groupby('movie_id').aggregate(['mean', 'count'])['rating']
df = df[df['count'] > 30].nlargest(10, 'mean')
movies.set_index('movie_id').loc[df.index.values]['title']