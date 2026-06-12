# 2. ATM Simulation System (While Loop)
# Create a menu-driven ATM with balance check, deposit, withdraw and exit options.
print("\tWelcome to the HDFC bank ATM")
login = int(input("For Using ATM type 1\n"))
Balance = 100000
deposit = 0
withdraw = 0
while login == 1 or 0 or 5:
    name = input("Enter the Name (Format - First Name"")"":- ")
    if name == "Yash":
        print(f"Welcome Mr. {name} to HDFC Bank Exclusive ATM")
        pin = int(input("Enter your 4 Digit Pin:- "))
        if pin == 2224:
            main_menu = 4
            while main_menu == 4:
                main_menu = int(input("Please kindly select any one option to procced \n1.Balance Check \n2.Deposit \n3.Withdraw \n4.Main Menu \n5.Log out\n"))
                if main_menu == 1:
                    print(f"Account Balance:- {Balance}")
                    main_menu = 4
                elif main_menu == 2:
                    deposit = int(input("How much amount do you have to Deposit: "))
                    if deposit >=0:
                        print(f"Amount has been successfully deposited\nBalance:- {Balance+deposit}")
                    main_menu = 4
                elif main_menu == 3:
                    withdraw = int(input("How much amount do you have to Withdraw"))
                    if withdraw <= Balance:
                        print(f"Withdraw Successful of ₹{withdraw}\nBalance Remaining:- {Balance-withdraw}")
                    else:
                        print("Insufficent Account")
                    main_menu = 4
                elif main_menu == 4:
                    print("Back to Main menu")
                    main_menu = 4
                elif main_menu == 5:
                    print("Log out Successfully")
                    login = 5
                

