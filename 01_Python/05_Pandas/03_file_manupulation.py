import pandas as pd 

# reading a csv file
df = pd.read_csv('data.csv')

print(df)


print(df.head(3))

print(df.tail(3))

print(df.describe())

print(df.info())

#  handling missing values
print(df.isnull())
print(df.isnull().any(axis=1))
print(df.isnull().sum())
print(df.notnull().sum())