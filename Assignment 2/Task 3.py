# 3. Search a Student Record and Stop When Found (Break)
# Search a student name and stop immediately when found.

print("\tWelcome to Student Record Finder")
student = ["Yash",
           "Om",
           "Atharv",
           "Kunal",
           "Saheel",
           "Sanskar ",
           "Kunal",
           "Ankit"]
Name = input("Which Student record you want to search:- ")
while Name in student:
    a = student.index(Name)
    print(f"Record found related to {student[a]}")
    break