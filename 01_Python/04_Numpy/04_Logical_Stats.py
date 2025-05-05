# Some time we can use logical indexing to filter the data
import numpy as np

data = np.array([1, 2, 3, 4, 5])
print(data)

# We can use logical indexing to filter the data
condition = data[data > 2]
print(condition)

# We can use logical indexing to filter the data
condition = data[data % 2 == 0]
print(condition)