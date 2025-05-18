# Sales data Visualisation 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

print(df.head(5))

total_sales =  df.groupby('Product')['Sales'].sum()
print(total_sales)

total_sales.plot(kind = 'bar' , color = 'teal')
plt.show()

sales_trend = df.groupby('Date')['Sales'].sum().reset_index()
print(sales_trend)

sales_trend.plot(kind = 'line')
plt.show()

