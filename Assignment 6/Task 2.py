import pandas as pd
# 2) DataFrame Creation and Basic Operations
# # Create a DataFrame with the following employee data:
# employees = {
#     'emp_id': [101, 102, 103, 104, 105],
#     'name': ['Alice Johnson', 'Bob Smith', 'Carol Williams', 'David Brown', 'Eve Davis'],
#     'department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
#     'salary': [75000, 60000, 80000, 70000, 65000],
#     'experience': [5, 3, 8, 4, 2]
# }
employees = {
    'emp_id': [101, 102, 103, 104, 105],
    'name': ['Alice Johnson', 'Bob Smith', 'Carol Williams', 'David Brown', 'Eve Davis'],
    'department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'salary': [75000, 60000, 80000, 70000, 65000],
    'experience': [5, 3, 8, 4, 2]
}

# 1. Create the DataFrame
employees = pd.DataFrame(employees)
# 2. Set emp_id as the index
employees.index = employees['emp_id']
print(employees)
# 3. Add a new column 'salary_per_experience' (salary/experience)

employees["Salary_per_experience"] = employees['salary']/employees['experience']
print(employees)
# 4. Create a boolean column 'high_earner' for salaries > 70000
employees[bool('high_earner')] = employees['salary']>70000
print(employees)
# 4. Indexing and Selection Tasks
print(employees.iloc[1])
print(employees['emp_id'])
a = employees[employees['emp_id']==101]
print(a)
b = employees[employees['name'].isin(['Bob Smith'])]
print(b)