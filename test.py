if Choice == 3:
            print(f"\tWelcome to caving Account Service Mr.{Holder_Name}")
            fa = CurrentAccount(Account_Number,Holder_Name,Balance)
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