mask_gender = data['gender'] == 'M'
mask_age = data['age'] > 30
np.count_nonzero(data[mask_gender & mask_age]['rating'] > 4.5)