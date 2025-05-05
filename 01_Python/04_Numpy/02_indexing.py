import numpy as np 
# Indexing in array in Numpy
# every data in an array can be access using indexing


# Create a 2D array (3 rows, 4 columns) for demonstration
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Original array:")
print(arr)

# ===== BASIC INDEXING =====
# Syntax: arr[row_index, column_index]

# Access single element at row 1, column 2 (0-based indexing)
print("\nElement at row 1, column 2:", arr[1, 2])  # Returns 7

# Access entire row (row 0)
print("\nFirst row:", arr[0, :])  # Returns [1 2 3 4]
print("\nFirst row:", arr[0])  # Returns [1 2 3 4]

# Access entire column (column 3)
print("\nFourth column:", arr[:, 3])  # Returns [4 8 12]

# ===== SLICING =====
# Syntax: arr[start:stop:step, start:stop:step]

# Get first two rows and first three columns
print("\nFirst 2 rows, first 3 columns:")
print(arr[:2, :3])  # Returns [[1 2 3], [5 6 7]]

# Get every other row and every other column
print("\nEvery other row and column:")
print(arr[::2, ::2])  # Returns [[1 3], [9 11]]

# ===== ADVANCED INDEXING =====
# Boolean indexing - select elements > 5
print("\nElements greater than 5:")
print(arr[arr > 5])  # Returns [6 7 8 9 10 11 12]

# Fancy indexing - select specific rows/columns
print("\nRows 0 and 2, columns 1 and 3:")
print(arr[[0, 2], :][:, [1, 3]])  # Returns [[2 4], [10 12]]

# ===== EDGE CASES =====
# Negative indices count from end
print("\nLast row, second column:", arr[-1, -3])  # Returns 10

# Omitting indices returns entire array
print("\nEntire array (using :):")
print(arr[:, :])