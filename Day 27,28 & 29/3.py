import pandas as pd
employees = {
    'emp_id': ['101.1', '102.1', '103', '104', '105'],
    'Date': ['2026-05-13','2026-04-24','2025-06-30','2026-03-26','2026-05-20'],
    'name': ['Alice','Bob','Alice','Charile','Bob'],
    'department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'salary': [75000, 60000, 80000, 70000, 65000],
    'experience': [5, 3, 8, 4, 2],
    'TF':[True,False,False,True,True]
}
employees = pd.DataFrame(employees)
print(employees.duplicated())
print(employees.duplicated().sum())
print(employees.duplicated(['name']).sum())

name_Clean = employees.drop_duplicates(['name'])
print(name_Clean)
last_clear = employees.drop_duplicates(keep="first")
print(last_clear)

reset = employees.drop_duplicates().reset_index()
print(reset)

a = pd.to_numeric(employees['emp_id'])
print(a)
employees['Date']=pd.to_datetime(employees['Date'])
employees['TF']=employees['TF'].astype(bool)
print(employees)
employees['department'].astype('category')
print(employees)
employees['experience']=pd.to_numeric(employees['experience'],errors="coerce")
employees_rename = employees.rename(columns={'name':'Name'})
print(employees_rename)
employees_1=employees.rename(columns={'department':'Department'})
print(employees_1)
# drop column
employees_2 = employees.drop(columns=['department'])
print(employees_2)
# Drop row
drop_row_employee = employees.drop([0,2])
print(drop_row_employee)

def square(x):
    return x**2
df = {
    "a":[1,2,3,4],
    "b":[10,20,30,40]
}
df = pd.DataFrame(df)
a = df.apply(square)
print(a)
#apply to specific column
b = df.apply(square(a))

