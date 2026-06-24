from abc import ABC,abstractmethod

class Student(ABC):
    def __init__(self,Roll_Number,Student_Name,Marks):
        self.Roll_Number = Roll_Number
        self.Student_Name = Student_Name
        self.__Marks = Marks

    @abstractmethod
    def calculate_percentage(self):
        pass

    def show_result(self):
        print(f"Student Result\n1.Roll Number: {self.Roll_Number}\n2.Student Name: {self.Student_Name}\n3.Marks: {self.__Marks}")

class ScienceStudent(Student):
    def __init__(self, Roll_Number, Student_Name, Marks):
        super().__init__(Roll_Number, Student_Name, Marks)

    def calculate_percentage(self):
        Percentage = (self._Student__Marks / 500) * 100
        print(f"Message!!\nScience Percentage: {Percentage}%")
        return super().show_result()

class CommerceStudent(Student):
    def __init__(self, Roll_Number, Student_Name, Marks):
        super().__init__(Roll_Number, Student_Name, Marks)

    def calculate_percentage(self):
        Percentage = (self._Student__Marks / 600) * 100
        print(f"Message!!\nCommerce Percentage: {Percentage}%")
        return super().show_result()

class ArtsStudent(Student):
    def __init__(self, Roll_Number, Student_Name, Marks):
        super().__init__(Roll_Number, Student_Name, Marks)

    def calculate_percentage(self):
        Percentage = (self._Student__Marks / 700) * 100
        print(f"Message!!\nArts Percentage: {Percentage}%")
        return super().show_result()

Roll_Number = int(input("Enter Roll Number: "))
Student_Name = input("Enter Student Name: ")
Marks = int(input("Enter Marks: "))

Student_Type = int(input("Select Student Type\n1.Science Student\n2.Commerce Student\n3.Arts Student\n"))

if Student_Type == 1:
    M = ScienceStudent(Roll_Number,Student_Name,Marks)
    M.calculate_percentage()
elif Student_Type == 2:
    M = CommerceStudent(Roll_Number,Student_Name,Marks)
    M.calculate_percentage()
elif Student_Type == 3:
    M = ArtsStudent(Roll_Number,Student_Name,Marks)
    M.calculate_percentage()
else:
    print("Wrong Information!!")