import pandas as pd

# merging dataframes

df1 = pd.DataFrame({'Key': ['A', 'B', 'C'], 'Value': [1, 2, 3]})
df2 = pd.DataFrame({'Key': ['A', 'B', 'D'], 'Value': [4, 5, 6]})

merged_df = pd.merge(df1, df2, on='Key', how='inner')
print(merged_df)

merged_df = pd.merge(df1, df2, on='Key', how='outer')
print(merged_df)

merged_df = pd.merge(df1, df2, on='Key', how='left')
print(merged_df)

merged_df = pd.merge(df1, df2, on='Key', how='right')
print(merged_df)
