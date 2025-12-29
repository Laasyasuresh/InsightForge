import pandas as pd

df = pd.read_csv(r"C:\Users\LASYAA\OneDrive\DS Proj\InsightForge\insightforge_dataset.csv")
print(df.head())
print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())
print("\nShape (rows, columns):")
print(df.shape)
print("\nColumn names:")
print(df.columns)
print("\nDataset info:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

print("\nUpdated data types:")
print(df.info())
df = df.sort_values(by='Order_Date')

print("\nData sorted by date:")
print(df[['Order_ID', 'Order_Date']].head())

df.to_csv(r"C:\Users\LASYAA\OneDrive\DS Proj\InsightForge\insightforge_dataset.csv", index=False)
print("\nCleaned dataset saved successfully")

# ===============================
# STEP 4: BUSINESS KPIs
# ===============================

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
avg_order_value = df['Sales'].mean()
total_orders = df['Order_ID'].nunique()

print("\n--- BUSINESS KPIs ---")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Order Value:", round(avg_order_value, 2))
print("Total Orders:", total_orders)

sales_by_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(sales_by_category)

profit_by_region = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print("\nProfit by Region:")
print(profit_by_region)

top_customers = df.groupby('Customer_ID')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Customers by Sales:")
print(top_customers)

import matplotlib.pyplot as plt

# ===============================
# CREATE & SAVE CHART 1
# ===============================
sales_by_category = df.groupby('Category')['Sales'].sum()

plt.figure()
sales_by_category.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# ===============================
# CREATE & SAVE CHART 2
# ===============================
profit_by_region = df.groupby('Region')['Profit'].sum()

plt.figure()
profit_by_region.plot(kind='bar')
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("profit_by_region.png")
plt.show()
