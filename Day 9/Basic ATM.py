print("\tWELCOME TO THE BOI BANK")
name = input("Enter your name: ")
Balance = 50000

if name == "Atharv" or "Atharv":
    print(f"Welcome Mr {name}")
    pin = int(input("Enter your pin: "))
    if pin == 2224:
        print(f"Hello Mr {name}, available balance is {Balance}")
        amount = int(input("How much amount do you have to withdraw: "))
        transcation_code = int(input("Enter the transcation pin: "))
        if transcation_code == 1011:
            print(f"{amount} has been deducted from your account mr {name}")
            print(f"Avaible balance is {Balance-amount}")
        else: 
            print("Please enter the correct transcation pin")
else:
    print("Your account does not exist at our bank")
         
         