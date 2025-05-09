import pandas as pd

# Dataframe is a two-dimensional labeled data structure with columns of potentially different types
data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
df = pd.DataFrame(data)
print(df)


# Import the pandas library (typically done at the top of the script)
import pandas as pd

# Create a dataframe from a list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Print the entire DataFrame
# This will display all rows and columns in a tabular format
print("Entire DataFrame:")
print(df)
# Output:
#      Name  Age         City
# 0   Alice   25     New York
# 1     Bob   30  Los Angeles
# 2 Charlie   35      Chicago

# Print just the 'Name' column
# This shows how to access a single column using square bracket notation
print("\nName column:")
print(df['Name'])
# Output:
# 0     Alice
# 1       Bob
# 2    Charlie

# Print just the 'Age' column
print("\nAge column:")
print(df['Age'])
# Output:
# 0    25
# 1    30
# 2    35

# Print just the 'City' column
print("\nCity column:")
print(df['City'])
# Output:
# 0       New York
# 1    Los Angeles
# 2        Chicago

# Print the first row using label-based indexing (loc)
# loc accesses rows by their index label (in this case 0)
print("\nFirst row (using loc):")
print(df.loc[0])
# Output:
# Name        Alice
# Age           25
# City    New York

# Print the first row using integer position-based indexing (iloc)
# iloc accesses rows by their numerical position (0 = first row)
print("\nFirst row (using iloc):")
print(df.iloc[0])
# Output is identical to loc in this case:
# Name        Alice
# Age           25
# City    New York

print("\n Specific data from specific row:")
print(df.at[1 ,'Age'])

# Accessing specific data from specific row using iloc
print("\nSpecific data from specific row:")
print(df.iat[1, 1])


# Data Mandipulation with dataframe
print("\nData Manipulation with dataframe:\n")
print(df)

# adding new column
print("\nAdding new column:\n")
df['Salary'] = [10000, 20000, 30000]
print(df)

# Removing column
print("\nRemoving column:\n")
df.drop('Salary', axis=1, inplace=True)
print(df)

# Add some years to the age column
print("\nAdding some years to the age column:\n")
df['Age'] += 5
print(df)

# Remove a row by index
print("\nRemove a row by index:\n")
df.drop(2, inplace=True)
print(df)