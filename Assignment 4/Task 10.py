from abc import ABC,abstractmethod

class Ticket(ABC):
    def __init__(self,Booking_ID,Customer_Name,Base_Price):
        self.Booking_ID = Booking_ID
        self.Customer_Name = Customer_Name
        self.__Base_Price = Base_Price

    @abstractmethod
    def ticket_price(self):
        pass

    def show_booking_details(self):
        print(f"Booking Details\n1.Booking ID: {self.Booking_ID}\n2.Customer Name: {self.Customer_Name}\n3.Base Price: {self.__Base_Price}")

class SilverTicket(Ticket):
    def __init__(self, Booking_ID, Customer_Name, Base_Price):
        super().__init__(Booking_ID, Customer_Name, Base_Price)

    def ticket_price(self):
        Total_Price = self._Ticket__Base_Price + 50
        print(f"Message!!\nSilver Ticket Price: {Total_Price}")
        return super().show_booking_details()

class GoldTicket(Ticket):
    def __init__(self, Booking_ID, Customer_Name, Base_Price):
        super().__init__(Booking_ID, Customer_Name, Base_Price)

    def ticket_price(self):
        Total_Price = self._Ticket__Base_Price + 150
        print(f"Message!!\nGold Ticket Price: {Total_Price}")
        return super().show_booking_details()

class PlatinumTicket(Ticket):
    def __init__(self, Booking_ID, Customer_Name, Base_Price):
        super().__init__(Booking_ID, Customer_Name, Base_Price)

    def ticket_price(self):
        Total_Price = self._Ticket__Base_Price + 300
        print(f"Message!!\nPlatinum Ticket Price: {Total_Price}")
        return super().show_booking_details()

Booking_ID = int(input("Enter Booking ID: "))
Customer_Name = input("Enter Customer Name: ")
Base_Price = int(input("Enter Base Price: "))

Ticket_Type = int(input("Select Ticket Type\n1.Silver Ticket\n2.Gold Ticket\n3.Platinum Ticket\n"))

if Ticket_Type == 1:
    M = SilverTicket(Booking_ID,Customer_Name,Base_Price)
    M.ticket_price()
elif Ticket_Type == 2:
    M = GoldTicket(Booking_ID,Customer_Name,Base_Price)
    M.ticket_price()
elif Ticket_Type == 3:
    M = PlatinumTicket(Booking_ID,Customer_Name,Base_Price)
    M.ticket_price()
else:
    print("Wrong Information!!")