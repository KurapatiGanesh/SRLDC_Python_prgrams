import pandas as pd

# Create a DataFrame with sales data
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'Category': ['Electronics', 'Furniture', 'Electronics', 'Furniture', 'Electronics'],
    'Sales': [1200, 800, 1500, 600, 1800]
}

df = pd.DataFrame(data)

print("Original dataFrame:")
print(df)

total_sale=df.groupby('Category')['Sales'].sum()
print(total_sale)