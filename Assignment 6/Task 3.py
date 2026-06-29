import pandas as pd
# Tasks using loc: 
student = {
            'ID':[5,10,15,20,25],
            'Name':["Om",'Kunal','Sakshi','Atharv','Yash'],
            'Science':[90,70,80,50,85],
            'Math':[85,79,54,78,86]}
student = pd.DataFrame(student,index=student['ID'])
print(student)
# 1. Select students with IDs 5, 10, 15 #
a = student.loc[[5,10,15]]
print(a)
# 2. Select math and science scores for students 1-10 # 
print(student.loc[5:10,['Math','Science']])
# 3. Select all data for students with math score > 80 # 
print(student.loc[student['Math']>80])
# iloc:  
# 4. Select first 5 students and first 3 subject columns 
print(student.iloc[:5,0:3])
# 5. Select every 3rd student
print(student.iloc[:,3]) 
# 6. Select last 3 students and last 2 columns 

