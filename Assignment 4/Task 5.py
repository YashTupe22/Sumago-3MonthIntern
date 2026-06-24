from abc import ABC,abstractmethod
class Payment(ABC):
    def __init__(self,Transcation_id,amount):
        self.Transcation_id = Transcation_id
        self.__amount = amount
    
    @abstractmethod
    def make_payment(self):
        pass

    def showtranscation(self):
        print(f"Transcation Detail\n1.Transcation id: {self.Transcation_id}\n2.Amount {self.__amount}")

class UPIPayment(Payment):
    def __init__(self, Transcation_id, amount):
        super().__init__(Transcation_id, amount)
    
    def make_payment(self):
        print("Message!!\nPayment is completed using UPI")
        return super().showtranscation()
 
class CreditCardPayment(Payment):
    def __init__(self, Transcation_id, amount):
        super().__init__(Transcation_id, amount)
    
    def make_payment(self):
        print("Message!!\nPayment is completed using Credit Card")
        return super().showtranscation()
 
class NetBankingPayment(Payment):
    def __init__(self, Transcation_id, amount):
        super().__init__(Transcation_id, amount)
    
    def make_payment(self):
        print("Message!!\nPayment is completed using Net Banking")
        return super().showtranscation()

Transcation_id = int(input("Enter your Transcation ID: "))
Amount = int(input("Enter your Amount: "))
Payment_method = int(input("Select Payment Method\n1.UPI\n2.Credit Card\n3.Net Banking\n"))
if Payment_method == 1:
    M = UPIPayment(Transcation_id,Amount)
    M.make_payment()
elif Payment_method == 2:
    M = CreditCardPayment(Transcation_id,Amount)
    M.make_payment()
elif Payment_method == 3:
    M = NetBankingPayment(Transcation_id,Amount)
    M.make_payment()
else:
    print("Wrong Information!!")