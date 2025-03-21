import pandas as pd 
data={
    'Name':["Ram","Pravin","Vijay","Navin","Vijay","Ram"],
    "Age":[34,54,45,67,78,34],
    "city":["Mumbai","Pune","Banglore","Chennai","Mumabi","Mumbai"]
}
df=pd.DataFrame(data)
print("Original Data:")
print(df)
unique_data=df.drop_duplicates()
print("Unique data:")
print(unique_data)