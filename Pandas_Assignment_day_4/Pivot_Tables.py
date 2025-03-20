import pandas as pd

# Create a DataFrame with sales data
data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'East', 'South', 'West'],
    'Product': ['Product A', 'Product B', 'Product A', 'Product B', 'Product B', 'Product A', 'Product A', 'Product B'],
    'Sales': [200, 150, 180, 220, 210, 190, 160, 240]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original Sales DataFrame:")
print(df)

pivot_table = pd.pivot_table(df, values='Sales', index='Region', columns='Product', aggfunc='sum', fill_value=0)
print("\nPivot Table (Total Sales per Region and per Product):")
print(pivot_table)
