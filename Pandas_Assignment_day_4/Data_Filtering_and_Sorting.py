import pandas as pd 

data = {
    'Employee Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales'],
    'Salary': [55000, 60000, 45000, 75000, 80000]
}
df=pd.DataFrame(data)
print("Original data Frame:")
print(df)

filltered_df=df[df['Salary']>50000]
sorted_df=filltered_df.sort_values(by='Salary',ascending=False)
print("Fillterd and Sorted DataFrame:")
print(sorted_df)