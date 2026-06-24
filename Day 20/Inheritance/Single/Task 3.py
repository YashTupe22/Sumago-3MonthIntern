class Student:
    def fetch(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

class Result(Student):
    def Display_Result(self,marks):
        print(f"\tResult\n1.Name: {self.name}\n2.Roll No: {self.roll_no}\n3.Total Marks: {marks}\n4.Percentage: {(marks)*100/500}")

name = input("Enter your name: ")
roll_no = int(input("Enter your roll no: "))
marks = int(input("Enter your Total Marks for 5 Subject: "))
r = Result()
r.fetch(name,roll_no)
r.Display_Result(marks)
