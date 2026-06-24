from abc import ABC,abstractmethod

class Order(ABC):
    def __init__(self,Order_ID,Product_Name,Product_Price):
        self.Order_ID = Order_ID
        self.Product_Name = Product_Name
        self.__Product_Price = Product_Price

    @abstractmethod
    def calculate_total(self):
        pass

    def show_order_details(self):
        print(f"Order Details\n1.Order ID: {self.Order_ID}\n2.Product Name: {self.Product_Name}\n3.Product Price: {self.__Product_Price}")

class LocalOrder(Order):
    def __init__(self, Order_ID, Product_Name, Product_Price):
        super().__init__(Order_ID, Product_Name, Product_Price)

    def calculate_total(self):
        Shipping_Charge = 50
        Total = self._Order__Product_Price + Shipping_Charge
        print(f"Message!!\nTotal Amount: {Total}")
        return super().show_order_details()

class StateOrder(Order):
    def __init__(self, Order_ID, Product_Name, Product_Price):
        super().__init__(Order_ID, Product_Name, Product_Price)

    def calculate_total(self):
        Shipping_Charge = 100
        Total = self._Order__Product_Price + Shipping_Charge
        print(f"Message!!\nTotal Amount: {Total}")
        return super().show_order_details()

class InternationalOrder(Order):
    def __init__(self, Order_ID, Product_Name, Product_Price):
        super().__init__(Order_ID, Product_Name, Product_Price)

    def calculate_total(self):
        Shipping_Charge = 500
        Total = self._Order__Product_Price + Shipping_Charge
        print(f"Message!!\nTotal Amount: {Total}")
        return super().show_order_details()

Order_ID = int(input("Enter Order ID: "))
Product_Name = input("Enter Product Name: ")
Product_Price = int(input("Enter Product Price: "))

Order_Type = int(input("Select Order Type\n1.Local Order\n2.State Order\n3.International Order\n"))

if Order_Type == 1:
    M = LocalOrder(Order_ID,Product_Name,Product_Price)
    M.calculate_total()
elif Order_Type == 2:
    M = StateOrder(Order_ID,Product_Name,Product_Price)
    M.calculate_total()
elif Order_Type == 3:
    M = InternationalOrder(Order_ID,Product_Name,Product_Price)
    M.calculate_total()
else:
    print("Wrong Information!!")