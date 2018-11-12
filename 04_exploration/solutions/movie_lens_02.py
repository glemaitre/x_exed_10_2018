data[data['rating'] > 4.5].groupby('gender').count()['rating']
