# Membership Operators
# 1. Student Search System
Student = ["Yash","Atharv","Kunal","Sujal","Om"]
s_name = input("Enter the Student name to be searched")
if(s_name in Student):
    print("Student name is found in the system")
else: 
    print("Student name not found in the system")

# 2. Employee Record Search
Employee = ["Yash","Atharv","Kunal","Sujal","Om"]
s_name = input("Enter the Employee name to be searched")
if(s_name in Student):
    print("Employee name is found in the system")
else: 
    print("Employee name not found in the system")
# 3. Product Availability Checker
products = ['pen', 'notebook', 'eraser', 'pencil']
p = input('Enter product name to check: ')

if p in products:
    print(p, 'is available')
else:
    print(p, 'is not available')
# 4. Library Book Search
books = ['Maths Basics', 'Physics Intro', 'Chemistry 101', 'English Grammar']
title = input('Enter book title to search: ')

if title in books:
    print('Book is available in library')
else:
    print('Book is not available')
# 5. Course Enrollment Verification
courses = ['Python', 'Data Science', 'Web Development']
course = input('Enter course name to check enrollment: ')

if course in courses:
    print('You are enrolled in', course)
else:
    print('You are not enrolled in', course)
