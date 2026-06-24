class BankAccount:
    name = input("Enter Account Holder name: ")
    acc_no = int(input("Enter Account no: "))
    bal = int(input("Enter your balance amount"))
    print(f"Details \nName: {name} \nAccount no: {acc_no} \nBalance amount: {bal}")

bank = BankAccount()

#MEthod 2
class BankAccount1:
    name = ""
    acc_no = 0
    bal = 0
    
b=BankAccount1()
b.name = input("Enter Account Holder name: ")
b.acc_no = int(input("Enter Account no: "))
b.bal = int(input("Enter your balance amount"))
print(f"Details \nName: {b.name} \nAccount no: {b.acc_no} \nBalance amount: {b.bal}")
