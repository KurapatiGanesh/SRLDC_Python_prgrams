import pandas as pd 
import numpy as np
data={
    "Maths":[67,np.nan,78,56,89],
    "Science":[78,90,88,np.nan,95],
    "History":[67,89,48,90,np.nan]
}

df=pd.DataFrame(data)

print("Display Original Missing values:")
print(df)

df_filled_mean=df.fillna(df.mean())
print("Filled Mean:",df_filled_mean)
df_filled_medium=df.fillna(df.median())
print("Filled  Median:",df_filled_medium)