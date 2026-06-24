class Employee:
    def display_employee(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"Employee's Basic Details:\n1.Name: {self.name}\n 2.Salary: {self.salary}")

class Manager(Employee):
    def display_manager(self,department):
        self.department = department
        print(f"Employer {self.name} works in {department}")

a = Manager()
name = input("Enter your Name: ")
sal = int(input("Enter your Salary: "))
a.display_employee(name,sal)
detail = input("Enter your department name: ")
a.display_manager(detail)
