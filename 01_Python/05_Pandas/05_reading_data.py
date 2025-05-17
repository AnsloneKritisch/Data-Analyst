import pandas as pd

# to read  url you need to install lxml
# pip install lxml

url = "https://www.fdic.gov/bank-failures/failed-bank-list"
df = pd.read_html(url)
print(df)

url = "https://en.wikipedia.org/wiki/Mobile_country_code"
df = pd.read_html(url , match = "Country" , header=0)
print(df)

# to read a excel file you need to install openpyxl
# pip install openpyxl

df = pd.read_excel("excel_data.xlsx")
print(df)

# Converting excel to pickle
# Advantages of using a pickle
# Speed boost when you need to reload the same dataset repeatedly inside Python scripts or notebooks.
# Smaller footprint (often 20‑50 % smaller than the original Excel).
# Preserves exact data types without extra parsing logic.

df.to_pickle("pickle_data.pkl")
df = pd.read_pickle("pickle_data.pkl")
print(df)