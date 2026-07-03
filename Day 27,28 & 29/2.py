import pandas as pd
import numpy as np
# DataFrame Creation and Basic Operations
# Create a DataFrame with the following employee data:
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
employees['salary_per_experience'] = employees['salary']/employees['experience']
print(employees)
# 4. Create a boolean column 'high_earner' for salaries > 70000
employees["high_earner"] = employees['salary']>70000
print(employees)
# 5. Display the DataFrame info and basic statistics
# 		3) Data Loading Tasks
# 			Create sample data and practice file operations: # 
#1. Create a DataFrame with sales data (date, product, quantity, price, region) 
sales_data = {
    'Date':['15/06/2026'],
    'Product':["Carplay Subscription"],
    'Quantity':[5],
    'Price':[6500],
    'Region' : ["India"]
}
sales_data = pd.DataFrame(sales_data)
#2. Save it as 'sales_data.csv' sal
sales_data.to_csv("/run/media/yash-tupe/Local Disk E/Linux/Sumago Python/Day 27/sales_data.csv")
#3. Read the CSV back with different parameters: 
#Skip the first row 
#Read only first 10 rows 
#Set date as index 
#Handle missing values as 'Unknown' 
#4. Save only specific columns to a new CSV file
# 2.	Basic info 
# (shape, dtypes, memory usage) 
# 3.	Missing value analysis (count and percentage) 
# 4.	Statistical summary for numeric columns 
# 5.	Unique value counts for categorical columns 
# 6.	Data quality issues (negative ages, outliers) 
# 7. Create visualizations for data distribution # 
# 8. Identify columns that need cleaning