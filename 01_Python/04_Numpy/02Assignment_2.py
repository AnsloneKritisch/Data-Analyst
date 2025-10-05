
### Assignment 2: Array Indexing and Slicing
# 1. Create a NumPy array of shape (6, 6) with values from 1 to 36. Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.
# 2. Create a NumPy array of shape (5, 5) with random integers. Extract the elements on the border.

import numpy as np

# 1. Create a NumPy array of shape (6, 6) with values from 1 to 36. Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.

# solution :
arr = np.arange(1, 37).reshape(6, 6)
print("Original Array:\n", arr)

# Extracting the sub-array (3rd to 5th rows and 2nd to 4th columns)
sub_array = arr[2:5, 1:4]
print("Sub-Array:\n", sub_array)


# 2. Create a NumPy array of shape (5, 5) with random integers. Extract the elements on the border.
# solution :
arr = np.random.randint(1, 100, size=(5, 5))
print("Original Array:\n", arr)

# Extracting the border elements
b1 = arr[0, :]  # Top row
b2 = arr[-1, :]  # Bottom row
b3 = arr[:, 0]  # Left column
b4 = arr[:, -1]  # Right column
print("Border Elements:\n", b1, b2, b3, b4)