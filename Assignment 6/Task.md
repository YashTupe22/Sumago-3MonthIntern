1)Pandas Series and DataFrames
Create the following Series and perform operations:
1. Create a Series of monthly temperatures: [22, 25, 28, 32, 35, 33, 30, 28, 26, 23, 20, 18]
# with index as month names ['Jan', 'Feb', ..., 'Dec']
2. Find the hottest and coldest months
3. Calculate the average temperature
4. Find months with temperature above 25°C
5. Create a new Series with temperature in Fahrenheit (F = C * 9/5 + 32)
2) DataFrame Creation and Basic Operations
# Create a DataFrame with the following employee data:
employees = {
    'emp_id': [101, 102, 103, 104, 105],
    'name': ['Alice Johnson', 'Bob Smith', 'Carol Williams', 'David Brown', 'Eve Davis'],
    'department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'salary': [75000, 60000, 80000, 70000, 65000],
    'experience': [5, 3, 8, 4, 2]
}
1. Create the DataFrame
2. Set emp_id as the index
3. Add a new column 'salary_per_experience' (salary/experience)
4. Create a boolean column 'high_earner' for salaries > 70000
4. Indexing and Selection Tasks
Tasks using loc: 
1. Select students with IDs 5, 10, 15 # 
2. Select math and science scores for students 1-10 # 
3. Select all data for students with math score > 80 # 
T4. Select first 5 students and first 3 subject columns 
5. Select every 3rd student 
6. Select last 3 students and last 2 columns asks using iloc:  
4. Select first 5 students and first 3 subject columns 
5. Select every 3rd student 
6. Select last 3 students and last 2 columns 
Boolean indexing tasks: 
7. Find students who scored above 85 in all subjects 
8. Find 12th graders with math score below 70 
9. Find students aged 17 or 18 with science score above average
5. Combine different selection methods
1. Find high-value orders (>$200) in Electronics category 
2. Select orders from last 30 days with discount > 15% 
3. Create a subset with only customer_name, order_value, and calculated profit 
4. Find customers who ordered both Electronics and Clothing