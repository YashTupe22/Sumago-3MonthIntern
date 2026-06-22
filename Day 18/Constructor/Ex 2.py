class Person:
    def __init__(self, name,sex, profession):
        
        self.name = name
        self.sex = sex
        self.profession = profession
    
    def show(self):
        print(f"Name: {self.name}\nSex: {self.sex}\nProfressional: {self.profession}")

    def work(self):
        print(f"{self.name} working as a {self.profession}")

d = Person("Yash","M","Software Engineering")
d.show()
d.work()