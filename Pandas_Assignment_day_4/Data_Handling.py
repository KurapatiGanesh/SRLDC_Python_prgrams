import pandas as pd
data={
    "Date":['2025-12-30','2020-08-17','2010-05-31','1999-12-06']
}
df=pd.DataFrame(data)
df['Date']=pd.to_datetime(df['Date'])

df['Year']=df['Date'].dt.year
df['Month']=df['Date'].dt.month
df['Day']=df['Date'].dt.day
print(df)