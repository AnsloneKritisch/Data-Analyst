import pandas as pd  

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data.csv')

# Display the entire DataFrame (first 5 and last 5 rows by default)
print(df)

# Display the first 3 rows of the DataFrame
print(df.head(3))

# Display the last 3 rows of the DataFrame
print(df.tail(3))

# Generate descriptive statistics (count, mean, std, min, max, etc.) for numeric columns
print(df.describe())

# Print concise summary of the DataFrame (column names, non-null counts, data types)
print(df.info())

# --- Handling Missing Values ---
# Check for missing values (returns a DataFrame of True/False for each cell)
print(df.isnull())

# Check if any row has missing values (returns True/False for each row)
print(df.isnull().any(axis=1))

# Count missing values per column
print(df.isnull().sum())

# Count non-missing values per column
print(df.notnull().sum())

# Display data types of each column
print(df.dtypes)

# --- Column Operations ---
# Rename the 'Date' column to 'Sale Date'
df = df.rename(columns={'Date': 'Sale Date'})
print(df.head(1))  # Show the first row after renaming

# Create a new column 'Value_new' by converting 'Value' to float (original may have missing values)
df['Value_new'] = df['Value'].astype(float)
print(df.head(1))

# Fill missing values in 'Value' with the column mean, then convert to int
df['Value_new'] = df['Value'].fillna(df['Value'].mean()).astype(int)
print(df.head(1))

# Add a new column 'New_data' with each 'Value' multiplied by 2 (lambda function)
df['New_data'] = df['Value'].apply(lambda x: x * 2)
print(df.head(1))

# --- Data Aggregation ---
# Group by 'Product' and calculate mean of 'Value' for each product
grouped_mean = df.groupby('Product')['Value'].mean()
print(grouped_mean)

# Group by 'Product' and 'Region', then calculate mean of 'Value' for each group
grouped_sum = df.groupby(['Product', 'Region'])['Value'].mean()
print(grouped_sum)

# Group by 'Region' and calculate multiple aggregations (mean, sum, count) for 'Value'
group_agg = df.groupby(['Region'])['Value'].agg(['mean', 'sum', 'count'])
print(group_agg)