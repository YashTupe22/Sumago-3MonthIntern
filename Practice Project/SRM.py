# Student Record Manager

# Concepts used: lists, tuples, sets, strings, loops later

# Features:

# Add student names
# Remove duplicates using sets
# Store marks
# Search student
# Find topper

student = []
a = input("Enter the Student name:- ")
b=a.split(",")
student.extend(b)
print("This may contain the students repeated name",student)
student_set = set(student)
print("without the students repeated name",student_set)
marks =()
b = input("Enter the score seperated by comma")
c = b.split(",")
marks = tuple(c)
print("Marks of the student",marks)
d = input("Student name to be searched")
print("Shows if the name of student is present or not ",d in student)
# Small algorithm see here index of student and marks is same so if student at index 0 have marks for index 0 of marks
a=max(marks)
b = marks.index(a)
print("Topper - name- ",student[b],"Marks - ",marks[b] )
