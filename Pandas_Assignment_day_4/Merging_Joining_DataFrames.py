import pandas as pd

# Create a DataFrame with employee details
employee_data = {
    'Employee ID': [101, 102, 103, 104],
    'Employee Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department ID': [1, 2, 1, 3]
}

employees_df = pd.DataFrame(employee_data)

# Create a DataFrame with department details
department_data = {
    'Department ID': [1, 2, 3],
    'Department Name': ['HR', 'Finance', 'Marketing']
}

departments_df = pd.DataFrame(department_data)

# Display the original DataFrames
print("Employee DataFrame:")
print(employees_df)

print("\nDepartment DataFrame:")
print(departments_df)
merged_df = pd.merge(employees_df, departments_df, on='Department ID', how='inner')
print(merged_df)