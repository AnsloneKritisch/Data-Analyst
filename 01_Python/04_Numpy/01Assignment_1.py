### Assignment 1: Array Creation and Manipulation

# 1. Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. Replace all the elements in the third column with 1.
# 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Replace the diagonal elements with 0.



# 1. Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. Replace all the elements in the third column with 1.

# Solution:
import numpy as np

# Create a 5x5 array with random integers between 1 and 20

arr = np.random.randint(1, 21, size=(5, 5))
print("Original Array:\n", arr)

# accessing the third column and replacing its elements with 1
# there are 2 ways to access the third column
# first way
third_column_1_way = arr[2]
print("Third Column before replacement:\n", third_column_1_way)
# second way
third_column_2_way = arr[:, 2]
print("Third Column before replacement:\n", third_column_2_way)

# replacing the third column with 1
arr[2] = 1
print("Array after replacing third column with 1:\n", arr)

# replacing the third column with 1 using the second way
# Change the 3rd row (index 2) to all 1s
arr[2, :] = 1
print("Array after replacing third column with 1 using the second way:\n", arr)





## 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Replace the diagonal elements with 0.

# Solution:

arr = np.random.randint(1, 17, size=(4, 4))
print("Original Array:\n", arr)

# replacing the diagonal elements with 0 using loop
# as we know there are total 4 diagonal elements in a 4x4 matrix
for i in range(4):
    arr[i, i] = 0
print("Array after replacing diagonal elements with 0 using loop:\n", arr)

# replacing the diagonal elements with 0 without using loop
np.fill_diagonal(arr, 0)
print("Array after replacing diagonal elements with 0:\n", arr)