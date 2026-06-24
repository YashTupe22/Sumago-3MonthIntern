class hod:
    def HOD(self):
        print("She is our HOD")

class teacher(hod):
    def teach(self):
        print("Mam teaches AI ML, and DSA")

class Student(teacher):
    def student(self):
        print("Yes I am her Student")

s1 = Student()
s1.teach()
s1.student()
s1.HOD()