from abc import ABC, abstractmethod

class FoodOrder(ABC):
    
    def __init__(self,OrderID,Name,_Foodprice,type):
        
        self.OrderID = OrderID
        self.Name = Name
        self.__Foodprice = _Foodprice
        self.type = type
        if self.type == "Veg" or "veg" or "VEG":
            self.gst = 0.05
        else:
            self.gst = 0.10

    @abstractmethod
    def generate_bill(self):
        pass

    def _resturant_details(self):
        print("Burger King")

    def __apply_discount(self,type):
        self.type = type
        if type == "Veg":
            self.discount = 10
            print(f"Discount is {self.discount}%")
        elif type == "Non Veg":
            self.discount = 5
            print(f"Discount is {self.discount}")
    
    def show_discount(self):
        print(f"Applied discount is {self.__apply_discount()}")
    
    def FinalBill(self):
        print(f"\tBills Details\nOrder id: {self.OrderID}\nCustomer Name: {self.Name}\n Total bill {self.__Foodprice*self.gst+(self.__Foodprice)}")

class VegOrder(FoodOrder):
    def generate_bill(self):
            print("Generating bill")
            bill = super().FinalBill()

id = int(input("Enter Order id: "))
name = input("Enter Customer Name: ")
foodprice = int(input("Enter Food Price: "))
type = input("Is food veg or non veg: ")
a = VegOrder(id,name,foodprice,type)
a.generate_bill()