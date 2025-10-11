### Assignment 1: DataFrame Creation and Indexing
# 1. Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers. Set the index to be the first column.
# 2. Create a Pandas DataFrame with columns 'A', 'B', 'C' and index 'X', 'Y', 'Z'. Fill the DataFrame with random integers and access the element at row 'Y' and column 'B'.

import pandas as pd

# 1. Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers. Set the index to be the first column.

data = {
    'Index': [1, 2, 3, 4, 5, 6],
    'A': [12, 7, 9, 14, 6, 11],
    'B': [5, 15, 8, 10, 3, 4],
    'C': [20, 25, 30, 35, 40, 45]
}

df = pd.DataFrame(data , index=data['Index'])
print("DataFrame with 4 columns and 6 rows:")
print(df)


# 2. Create a Pandas DataFrame with columns 'A', 'B', 'C' and index 'X', 'Y', 'Z'. Fill the DataFrame with random integers and access the element at row 'Y' and column 'B'.

data = {
    'A': [10, 20, 30],
    'B': [40, 50, 60],
    'C': [70, 80, 90]
    }

index = ['X', 'Y', 'Z']

df2 = pd.DataFrame(data, index)
print("\nDataFrame with columns 'A', 'B', 'C' and index 'X', 'Y', 'Z':")
print(df2)
element = df2.at['Y', 'B']
print(f"\nElement at row 'Y' and column 'B': {element}")




### Assignment 2: DataFrame Operations

# 1. Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers. Add a new column that is the product of the first two columns.
# 2. Create a Pandas DataFrame with 3 columns and 4 rows filled with random integers. Compute the row-wise and column-wise sum.

# 1. Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers. Add a new column that is the product of the first two columns.

data = {
    'A': [1, 2, 3, 4, 5], 
    'B': [6, 7, 8, 9, 10],
    'C': [11, 12, 13, 14, 15]
    }

df3 = pd.DataFrame(data)
df3['Product'] = df3['A'] * df3['B']
print("\nDataFrame with new column as product of first two columns:")
print(df3)

# 2. Create a Pandas DataFrame with 3 columns and 4 rows filled with random integers. Compute the row-wise and column-wise sum.

data = {
    'A': [2, 4, 6, 8], 
    'B': [1, 3, 5, 7],
    'C': [9, 11, 13, 15]
    }

df4 = pd.DataFrame(data)
row_sum = df4.sum(axis=1)
col_sum = df4.sum(axis=0)
print("\nDataFrame with row-wise and column-wise sum:")
print(df4)
print("Row-wise sum:\n",row_sum)
print("Column-wise sum:\n",col_sum)

# Accessing specific data from specific row
row_sum = df4.loc[2].sum()
print("Sum of row 2:", row_sum)