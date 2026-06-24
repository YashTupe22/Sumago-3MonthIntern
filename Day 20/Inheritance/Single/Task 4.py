class BankAccount:
    def details(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

class interest_Rate(BankAccount):
    def display(self,interest_Rate):
        self.interest_Rate = interest_Rate
        print(f"\tDetails\n1.Name: {self.account_holder}\n2.Balance: {self.balance}\n3.Interest you will be getting: {(self.balance*interest_Rate)/100} per year")

name = input("Enter Account Holder name: ")
balance = int(input("Enter Balance: "))
roi = int(input("Enter rate of interest: "))

roib = interest_Rate()
roib.details(name,balance)
roib.display(roi)