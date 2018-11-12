# However we should look at the ratios instead of the count
for gender_idx, df_group in data.groupby('gender'):
    count = np.count_nonzero(df_group[df_group['age'] > 30]['rating'] > 4.5)
    print('The ratio for {} is {:.2f}'
          .format(gender_idx, count / df_group.shape[0]))