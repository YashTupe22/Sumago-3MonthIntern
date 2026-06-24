from abc import ABC,abstractmethod
print("Bank Management System")
class Account(ABC):
    def __init__(self,Account_Number,Holder_Name,Balance):
        self.Account = Account_Number
        self.Name = Holder_Name
        self.__Balance = Balance
    
    @abstractmethod
    def calculate_interest(self):
        pass

    def deposit(self,amount):
        self.Amount = amount
        self.__Balance = self.__Balance+self.Amount
        print(f"Your Updated balance is {self.__Balance}")
    
    def withdraw(self,amount):
        self.Amount = amount
        self.__Balance = self.__Balance-self.Amount
        print(f"Your Updated balance is {self.__Balance}")

    def get_balance(self):
        print(f"Available Balance: {self.__Balance}")

class SavingAccount(Account):
    def calculate_interest(self):
        SA = self._account__Balance*0.04
        print(f"Interest is {SA}")

class CurrentAccount(Account):
    def calculate_interest(self):
        SA = self._account__Balance*0.12
        print(f"Interest is {SA}")

class FixedDeoositAccount(Account):
    def calculate_interest(self):
        SA = self._account__Balance*0.08
        print(f"Interest is {SA}")

print("Welcome to HDFC Bank")
loop_choice = True
while loop_choice == True:
    Account_Number = int(input("Enter your Account no:- "))
    Holder_Name = input("Enter account holder name:- ")
    Balance = int(input("Enter Balance:- "))   
    Choice = int(input("Which service you want to use\n1.Saving Account\n2.Current Account\n3.Fixed Deposit Account\n4.Exit\n"))
    while Choice == 1 or 2 or 3:
        if Choice == 1:
            print(f"\tWelcome to Saving Account Service Mr.{Holder_Name}")
            sa = SavingAccount(Account_Number,Holder_Name,Balance)
            choice = int(input("Main menu\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Calculate Interest"))
            if choice == 1:
                amount = int(input("How much amount you want to deposit:- "))
                sa.deposit(amount)
            elif choice == 2:
                amount = int(input("How much amount you want to Withdraw:- "))
                sa.withdraw(amount)
            elif choice == 3:
                sa.get_balance()
            elif choice == 4:
                sa.calculate_interest()
            else:
                print("Exiting to Login page")
                break

        elif Choice == 2:
            print(f"\tWelcome to Current Account Service Mr.{Holder_Name}")
            ca = CurrentAccount(Account_Number,Holder_Name,Balance)
            choice = int(input("Main menu\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Calculate Interest\n5.Log out\n "))
            if choice == 1:
                amount = int(input("How much amount you want to deposit:- "))
                ca.deposit(amount)
            elif choice == 2:
                amount = int(input("How much amount you want to Withdraw:- "))
                ca.withdraw(amount)
            elif choice == 3:
                ca.get_balance()
            elif choice == 4:
                ca.calculate_interest()
            else:
                print("Exiting to Login page")
                break

        elif Choice == 3:
            print(f"\tWelcome to Fixed Deposit Account Service Mr.{Holder_Name}")
            fa = CurrentAccount(Account_Number,Holder_Name,Balance)
            choice = int(input("Main menu\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.falculate Interest\n5.Log out\n "))
            if choice == 1:
                amount = int(input("How much amount you want to deposit:- "))
                fa.deposit(amount)
            elif choice == 2:
                amount = int(input("How much amount you want to Withdraw:- "))
                fa.withdraw(amount)
            elif choice == 3:
                fa.get_balance()
            elif choice == 4:
                fa.calculate_interest()
            else:
                print("Exiting to Login page")
                break
        else:
            loop_choice = False
            break