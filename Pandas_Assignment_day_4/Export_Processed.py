import pandas as pd 
data={
    "Name":["Ram","Vijay","Varun"],
    "Salary":[15000,17000,12000]
}
df=pd.DataFrame(data)
df['Bonus']=df['Salary']*0.10


df.to_excel('data.xlsx',index=False)
print("Export Data SucessFully")