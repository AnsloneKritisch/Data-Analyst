# Numpy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

# The name numpy is short for "Numerical Python" and it is often used in conjunction with packages like SciPy and Matplotlib for scientific computing.

# In numpy, arrays are the core data structure. An array is a collection of elements of the same data type, similar to a list, but with additional features such as multi-dimensional support and vectorized operations.

# Numpy arrays are also more efficient than lists, as they are stored in a contiguous block of memory, which results in faster access times and lower memory usage.

# Numpy provides a variety of functions for performing operations on arrays, such as mathematical functions, sorting, and reshaping.

# It also provides tools for integrating C/C++ and Fortran code, which makes it easier to use code written in these languages.

# In addition, numpy provides support for linear algebra operations, Fourier transform, and random number generation.

# Numpy is widely used in scientific computing, data analysis, machine learning, and many other fields.

# To install numpy we need to use pip install numpy

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Shape function help to get the no. of data 
print( arr1.shape) # the out put will be (5,) which means it is a 1D array with 5 elements
# we can reshape it to 5 rows and 1 column
print(arr1.reshape(1, 5))
# or the way i want it to be reshaped
print(arr1.reshape(5, 1))

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(arr2.shape)

# create an array with a range using arrange function 
arr3 = np.arange(0, 10 , 2)
print(arr3)

#after creating an array with a range using arrange function we can reshape it using reshape function
arr4 = np.arange(0, 10 , 2).reshape(5 ,1)
print(arr4)

# Create a 2D NumPy array with 3 rows and 4 columns of ones
arr5 = np.ones((3, 4))
print(arr5)

arr5 = np.ones((3, 4), dtype=int)
print(arr5)

# Create a 2D NumPy array with 3 rows and 4 columns of zeros
arr6 = np.zeros((3, 4))
print(arr6)

arr6 = np.zeros((3, 4), dtype=int)
print(arr6)

# Create a 2D NumPy array with 4 rows and 4 columns with 1s on the diagonal and 0s elsewhere
arr7 = np.eye(4)
print(arr7)


# Create a 2D NumPy array with 2 rows and 3 columns
# Outer list represents rows, inner lists represent column values
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Print the entire array with structure preserved
# Shows rows and columns clearly in output
print("Array:\n", arr)

# .shape - Returns dimensions as (rows, columns) for 2D arrays
# For N-dimensional arrays, returns a tuple with N elements
print("Shape:", arr.shape)  # Output: (2, 3)

# .ndim - Returns number of dimensions (axes)
# 1 for vectors, 2 for matrices, 3+ for tensors
print("Number of dimensions:", arr.ndim)  # Output: 2

# .size - Returns total elements (rows × columns)
# Works for arrays of any dimension
print("Size (number of elements):", arr.size)  # Output: 6

# .dtype - Shows data type of elements
# Common types: int32, int64, float32, float64, etc.
# Automatically determined from input values
print("Data type:", arr.dtype)  # Output: int64 (platform dependent)

# .itemsize - Returns memory used by each element in bytes
# Depends on dtype (int64 = 8 bytes, float32 = 4 bytes, etc.)
print("Item size (in bytes):", arr.itemsize)  # Output: 8 (for int64)

