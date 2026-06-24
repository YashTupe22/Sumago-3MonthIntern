class Student:
    def __init__(self,name):
        print("Inside Constructor ")
        self.name = name
        print("Variable Initialized")

    def show(self):
        print("Hello, my name is ",self.name)

s1 = Student("Yash")
s1.show()