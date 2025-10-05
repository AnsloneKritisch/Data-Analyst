import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = sns.load_dataset("titanic")
print(df.head())

# Visualization of age distribution
sns.histplot(df["age"], kde=True)
plt.show() 

# Mean value imputation
# Correct way to create a new column with mean-imputed values
df["Age_mean"] = df["age"].fillna(df["age"].mean())

# Compare the original and imputed columns
print(df[['Age_mean', 'age']].head())


# Median imputation
# Correct way to create a new column with median-imputed values
df["Age_median"] = df["age"].fillna(df["age"].median())
print(df[['Age_median', 'age']].head())