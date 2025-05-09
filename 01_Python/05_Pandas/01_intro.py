# What are pandas in Python?
# Pandas is a library providing data structures and functions to efficiently handle structured data, including tabular data such as spreadsheets and SQL tables.
# It is a very powerful library for data analysis and manipulation in Python.
# It provides data structures such as Series (one-dimensional labeled array), DataFrame (two-dimensional labeled data structure with columns of potentially different types) and Panel (three-dimensional labeled data structure).
# It also provides functions for filtering, grouping, sorting and performing statistical operations on data.

# Why is it important?
# It is important because it provides a convenient way to handle and manipulate structured data in Python.
# It is also very powerful because it allows performing statistical operations on data in a very efficient manner.
# It is also used for data analysis, data visualization and data mining.
# It is widely used in data science and data engineering.
# It is also used in machine learning and artificial intelligence.
# It is also used in web development and automation.
# It is also used in data visualization and reporting.

# To install pandas we need to use pip install pandas

import pandas as pd 

# Series is a one-dimensional labeled array
# DataFrame is a two-dimensional labeled data structure with columns of potentially different types
# Panel is a three-dimensional labeled data structure

# Create a Series object
series = pd.Series([1, 2, 3, 4, 5])
print(series)

# creata as series from dictonary
series = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(series)


data = [10 , 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index)
print(series)

