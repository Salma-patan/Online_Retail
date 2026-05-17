import pandas as pd
import matplotlib.pyplot as plt
import os

# Show files in current folder
print("FILES IN FOLDER:")
print(os.listdir())

# Load dataset
# Make sure the filename matches EXACTLY what you see in os.listdir()
df = pd.read_csv("Online_Retail.csv/online_retail.csv")

# Preview dataset
print("\nDATA PREVIEW:")
print(df.head())

# ---------------- DATA CLEANING ----------------

# Remove missing values
df = df.dropna()

# Remove cancelled invoices
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Remove negative quantities
df = df[df['Quantity'] > 0]

# ---------------- FEATURE ENGINEERING ----------------

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# ---------------- ANALYSIS ----------------

# Total Revenue
print("\nTOTAL REVENUE:")
print(df['Revenue'].sum())

# Top 10 products
print("\nTOP 10 PRODUCTS:")
top_products = (
    df.groupby('Description')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

# Top 10 countries by revenue
print("\nTOP 10 COUNTRIES:")
country_sales = (
    df.groupby('Country')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(country_sales)

# ---------------- VISUALIZATION ----------------

plt.figure(figsize=(12, 6))

top_products.plot(kind='bar')

plt.title("Top 10 Products")
plt.xlabel("Products")
plt.ylabel("Quantity Sold")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()