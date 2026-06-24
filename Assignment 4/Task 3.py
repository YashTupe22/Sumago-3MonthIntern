from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,Employee_ID,Employee_Name,Basic_Salary):
        self.Employee_id = Employee_ID
        self.Employee_Name = Employee_Name
        self.__Basic_salary = Basic_Salary

    @abstractmethod
    def calculate_salary(self):
        pass

    def show_details(self):
        print(f"\tDetails\n1.Employee Id: {self.Employee_id}\n2.Employee Name: {self.Employee_Name}\n3.Basic Salary: {self.__Basic_salary}")

class Manager(Employee):
    def __init__(self, Employee_ID, Employee_Name, Basic_Salary):
        super().__init__(Employee_ID, Employee_Name, Basic_Salary)
    def calculate_salary(self):
        bonus = self._Employee__Basic_salary*0.30
        print(f"Manager Bonus is {bonus}  and Total salary is {self._Employee__Basic_salary+bonus}")

class Developer(Employee):
    def __init__(self, Employee_ID, Employee_Name, Basic_Salary):
        super().__init__(Employee_ID, Employee_Name, Basic_Salary)
    def calculate_salary(self):
        bonus = self._Employee__Basic_salary*0.20
        print(f"Developer Bonus is {bonus} and Total salary is {self._Employee__Basic_salary+bonus}")

class Intern(Employee):
    def __init__(self, Employee_ID, Employee_Name, Basic_Salary):
        super().__init__(Employee_ID, Employee_Name, Basic_Salary)
    def calculate_salary(self):
        bonus = self._Employee__Basic_salary*0.05
        print(f"Intern Bonus is {bonus} and Total salary is {self._Employee__Basic_salary+bonus}")

emp_id = int(input("Enter your Employee ID: "))
ename = input("Enter your name: ")
sal = int(input("Enter your Salary: "))
des = int(input("What is your designation\n1.Manager\n2.Developer\n3.Intern"))
if des == 1:
    M = Manager(emp_id,ename,sal)
    M.show_details()
    M.calculate_salary()
elif des == 2:
    D = Developer(emp_id,ename,sal)
    D.show_details()
    D.calculate_salary()
elif des == 3:
    I = Intern(emp_id,ename,sal)
    I.show_details()
    I.calculate_salary()
else:
    print("Wrong Information!!")