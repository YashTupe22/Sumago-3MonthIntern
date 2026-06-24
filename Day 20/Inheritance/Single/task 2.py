class Vehicle:
    def fetch(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def display(self,fuel_type):
        self.fuel_type = fuel_type
        print(f"Details\n1.Brand: {self.brand}\n2.Model: {self.model}\n3.Fuel Type: {fuel_type}")

brand = input("Enter Car Brand Name:- ")
model = input("Enter Car Model Name:- ")
fuel_type = input("Enter Car fuel Type:- ")
c = Car()
c.fetch(brand,model)
c.display(fuel_type)