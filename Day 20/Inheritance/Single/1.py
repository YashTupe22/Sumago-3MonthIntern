class teacher:
    def teach(self):
        print("Mam teaches AI ML, and DSA")

class Student(teacher):
    def stud(self):
        print("Yes I am her Student")

s1 = Student()
s1.teach()
s1.stud()