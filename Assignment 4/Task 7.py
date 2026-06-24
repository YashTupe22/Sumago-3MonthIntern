from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,Vehicle_Number,Rent_Per_Day):
        self.Vehicle_Number = Vehicle_Number
        self.__Rent_Per_Day = Rent_Per_Day

    @abstractmethod
    def calculate_rent(self):
        pass

    def show_vehicle_details(self):
        print(f"Vehicle Details\n1.Vehicle Number: {self.Vehicle_Number}\n2.Rent Per Day: {self.__Rent_Per_Day}")

class Bike(Vehicle):
    def __init__(self, Vehicle_Number, Rent_Per_Day):
        super().__init__(Vehicle_Number, Rent_Per_Day)

    def calculate_rent(self):
        Days = int(input("Enter Number of Days: "))
        Total_Rent = Days * 500
        print(f"Message!!\nTotal Bike Rent: {Total_Rent}")
        return super().show_vehicle_details()

class Car(Vehicle):
    def __init__(self, Vehicle_Number, Rent_Per_Day):
        super().__init__(Vehicle_Number, Rent_Per_Day)

    def calculate_rent(self):
        Days = int(input("Enter Number of Days: "))
        Total_Rent = Days * 1500
        print(f"Message!!\nTotal Car Rent: {Total_Rent}")
        return super().show_vehicle_details()

class Bus(Vehicle):
    def __init__(self, Vehicle_Number, Rent_Per_Day):
        super().__init__(Vehicle_Number, Rent_Per_Day)

    def calculate_rent(self):
        Days = int(input("Enter Number of Days: "))
        Total_Rent = Days * 5000
        print(f"Message!!\nTotal Bus Rent: {Total_Rent}")
        return super().show_vehicle_details()

Vehicle_Number = input("Enter Vehicle Number: ")
Rent_Per_Day = int(input("Enter Rent Per Day: "))

Vehicle_Type = int(input("Select Vehicle\n1.Bike\n2.Car\n3.Bus\n"))

if Vehicle_Type == 1:
    M = Bike(Vehicle_Number,Rent_Per_Day)
    M.calculate_rent()
elif Vehicle_Type == 2:
    M = Car(Vehicle_Number,Rent_Per_Day)
    M.calculate_rent()
elif Vehicle_Type == 3:
    M = Bus(Vehicle_Number,Rent_Per_Day)
    M.calculate_rent()
else:
    print("Wrong Information!!")
