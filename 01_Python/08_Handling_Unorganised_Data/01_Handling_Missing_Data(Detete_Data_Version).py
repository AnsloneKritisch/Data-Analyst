# It is very imp to handle missing values in your data. 
# Basically we get raw and messy data - we need to clean it and make it ready for analysis

import seaborn as sns 

df = sns.load_dataset('titanic')
print(df.head(5))

# check missing values 
md = df.isnull().sum()
print(md)

# check how much data 
print(df.shape)

# one way to handle missing values is to remove rows with missing values
df = df.dropna()
print(df.shape)

# by removing rows with missing values is also decreases amount of data

# column-wise
df = df.dropna(axis = 1)
print(df.shape)