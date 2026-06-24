class Person:
    def fetch(self,name,age):
        self.name = name
        self.age = age

class Teacher(Person):
    def display(self,subject):
        self.subject = subject
        print(f"Detail\n1.Name {self.name}\n2.age {self.age}\n3.Subject taught: {subject}")

name = input("Enter your name: ")
age = int(input("Enter Age: "))
subject = input("Enter the name of subject taught: ")

t = Teacher()
t.fetch(name,age)
t.display(subject)

