import pandas as pd
import matplotlib.pyplot as plt

data={
    "Month":["jan","feb","March","April","May","Jun"],
    "Sales":[50000,40000,45000,70000,60000,65000]
}

df=pd.DataFrame(data)

plt.figure(figsize=(8,5))

df.plot(x='Month', y="Sales",kind='line' ,marker='o',color='g',linestyle='-' ,legend=False)
plt.title("Monthly Sales Tread:")
plt.xlabel('Month')
plt.ylabel('Sales ($)')

plt.grid(True)
plt.show()

plt.figure(figsize=(9,6))
df.plot(x='Month', y='Sales', kind='bar' , color='g', legend=False) 
plt.title("Monthly Sales Bar Chart:")
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

