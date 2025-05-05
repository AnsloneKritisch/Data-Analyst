# Normalization of data -> to have a mean of 0 and standard deviation of 1
# Standardization of data -> to have a mean of 0 and standard deviation of 1

import numpy as np

data = np.array([1, 2, 3, 4, 5])
print(data)

# mean function will return the mean of the data
mean = np.mean(data)
print("mean of data : ",mean)

# median function will return the median of the data
median = np.median(data)
print("median of data : ",median)

# var function will return the variance of the data
var = np.var(data)
print("variance of data : ",var)

# std function will return the standard deviation of the data
std = np.std(data)
print("standard deviation of data : ",std)

# Normalizing the data = (data - mean) / standard deviation
normalized_data = (data - mean) / std
print("normalized data : ",normalized_data)

# Srandardizing the data = (data - mean) / standard deviation
standardized_data = (data - np.mean(data)) / np.std(data)
print("standardized data : ",standardized_data)

