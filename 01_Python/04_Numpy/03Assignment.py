### Assignment 3: Statistical Operations

# 1. Create a NumPy array of shape (5, 5) filled with random integers. Compute the mean, median, standard deviation, and variance of the array.
# 2. Create a NumPy array of shape (3, 3) with values from 1 to 9. Normalize the array (i.e., scale the values to have a mean of 0 and a standard deviation of 1).


# 1. Create a NumPy array of shape (5, 5) filled with random integers. Compute the mean, median, standard deviation, and variance of the array.
# solution :
import numpy as np

arr = np.random.randint(1, 100, size=(5, 5))
print("Array:\n", arr)

mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)
var = np.var(arr)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)
print("Variance:", var)


# 2. Create a NumPy array of shape (3, 3) with values from 1 to 9. Normalize the array (i.e., scale the values to have a mean of 0 and a standard deviation of 1).
# solution :
arr = np.arange(1, 10).reshape(3, 3)
print("Array:\n", arr)

mean = np.mean(arr)
std = np.std(arr)
normalized_arr = (arr - mean) / std
print("Normalized Array:\n", normalized_arr)
print("Normalized Array (rounded 1st way):\n", np.round(normalized_arr, 2))
print("Normalized Array (rounded) 2nd way:\n", normalized_arr.round(2))