import pandas as pd
employees = {
    'emp_id': ['101.1', '102.1', '103', '104', '105'],
    'Date': ['2026-05-13','2026-04-24','2025-06-30','2026-03-26','2026-05-20'],
    'name': ['Alice','Bob','Alice','Charile','Bob'],
}
employees_joining = {
    'emp_id': ['101.1', '102.1', '106', '104', '105'],
    'department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'salary': [75000, 60000, 80000, 70000, 65000],
    'experience': [5, 3, 8, 4, 2],
}
employees = pd.DataFrame(employees)
employees_joining = pd.DataFrame(employees_joining)
# Basic Join
join = pd.merge(employees,employees_joining,on="emp_id")
print(join)
# Left join
left_join = pd.merge(employees,employees_joining,on="emp_id",how="left")
print(left_join)
# Right Join
right_join = pd.merge(employees,employees_joining,on="emp_id",how="right")
print(right_join)
# Outer Join
outer_join = pd.merge(employees,employees_joining,on="emp_id",how="outer")
print(outer_join)

# For Different Column
employees = {
    'emp_id': ['101.1', '102.1', '103', '104', '105'],
    'Date': ['2026-05-13','2026-04-24','2025-06-30','2026-03-26','2026-05-20'],
    'name': ['Alice','Bob','Alice','Charile','Bob'],
}
employees_joining = {
    'id': ['101.1', '102.1', '106', '104', '105'],
    'Date': ['2026-05-13','2026-04-24','2025-06-30','2026-03-26','2026-05-20'],
    'department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'salary': [75000, 60000, 80000, 70000, 65000],
    'experience': [5, 3, 8, 4, 2],
}
employees = pd.DataFrame(employees)
employees_joining = pd.DataFrame(employees_joining)

# Single Column Merge
merge_col = pd.merge(employees,employees_joining,left_on="emp_id",right_on="id")
print("Merge one",merge_col)

df1 = pd.DataFrame({"a":[1,2],'b':[3,4]})
df2 = pd.DataFrame({"a":[5,6],'b':[7,8]})
df3 = pd.DataFrame({"c":[9,10],'d':[11,12]})

concat_vertical = pd.concat([df1,df2])
print(concat_vertical)

concat_horizontally = pd.concat([df1,df2],axis=1)
print(concat_horizontally)

concat_horizontally = pd.concat([df1,df2],axis=1)
concat_ig_index  = pd.concat([df1,df2],axis=1,ignore_index=True)
print(concat_ig_index)

df1 = pd.DataFrame({"a":[1,2,3,4]},index=[1,2,3,4])
df2 = pd.DataFrame({"b":[5,6,7,8]},index=[1,2,3,4])
df3 = pd.DataFrame({"c":[9,10,11,12]},index=[1,2,3,4])

print(df1)
join = df1.join(df2)
print(join)

left_join = df1.join(df2,how='left')
print(left_join)

right_join = df1.join(df2,how="right")
print(right_join)

outer_join = df1.join(df2,how="outer")
print(outer_join)