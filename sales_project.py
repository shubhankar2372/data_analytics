# -*- coding: utf-8 -*-
"""sales_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dfXNm-60Ew4UWaIZVxLRKtQ_JU1lySyW
"""

from google.colab import files
files.upload()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Cleaned_Superstore.csv')

df

df.head(10)

df.columns

#cleaning data
df.dropna(inplace=True)

df['Revenue'] = df['Sales'] * df['Quantity']

df

#checking for columns

if 'Order_Date' in df.columns:
  print(['Order_Date'])
else:
  print("No such column exist")

#convert order date
df['Order_Date'] = pd.to_datetime(df['Order Date'], errors = 'coerce')

print(df['Order_Date'].dtypes)

# Convert column to datetime (just to be safe)
df['Order Date'] = pd.to_datetime(df['Order_Date'])

df = df.set_index('Order Date')

df.index = pd.to_datetime(df.index)

monthly = df.resample('ME')['Revenue'].sum()

print(monthly)

df

monthly_revenue = df.groupby('Month')['Revenue'].sum()

#MONTHLY REVENUE TRENDS
monthly_revenue.plot(kind='line', title='Monthly Revenue', color = 'green')
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

#TOP TEN PRODUCTS BY REVENUE
top_products = df.groupby('Product Name')['Revenue'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='bar', title='Top Ten Products by Revenue')
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

#PROFITS BY REGION
region_profit = df.groupby('Region')['Profit'].sum()
region_profit.plot(kind='pie', autopct='%1.1f%%', title='Profit by Region')
plt.ylabel("")
plt.tight_layout()
plt.show()