def audi(name,age):
        Audi_Q3_Deposit = 75000
        Audi_Q3_Rent = 30000

        Audi_A5_Deposit = 100000
        Audi_A5_Rent = 50000

        Audi_TT_Deposit = 200000
        Audi_TT_Rent = 100000
        print(f"Mr. {name} for Audi. We currently provide 3 best model of them for renting out\nModels:-\n1.Audi Q3\n2.Audi A5\n3.Audi TT")
        again = "No"
        while again == "no" or "No" or "N" or "n":
            car = int(input("Enter the serial no of selected model for futher detail:- "))
            if car==1:
                print(f"Audi Q3 Details:\n1.Comapany: Audi\n2.Type: SUV\n3.Mileage: 14KMPL\n4.Deposit: {Audi_Q3_Deposit}\n5.Rent(per day): {Audi_Q3_Rent}")
                rent = input("Do you want to rent this model:- ")
                if rent == "yes" or "Yes" or "YES" or "Y" or "y":
                    rentday = int(input("How many days do you want to rent the car:- "))
                    print(f"\tDelux Motor Pvt Ltd\n\tPune\nName:- {name}\nAge:- {age}\nLicense:- Yes\nRented Car:- Audi Q3\nNo of Day to be rented:-{rentday}\nBase Payment:- {Audi_Q3_Rent*rentday}\nDeposit:- {Audi_Q3_Deposit}\nTotal Payable amount:- {Audi_Q3_Deposit+(Audi_Q3_Rent*rentday)}")
            elif car==2:
                print(f"Audi A5 Details:\n1.Comapany: Audi\n2.Type: Sedan\n3.Mileage: 14KMPL\n4.Deposit: {Audi_A5_Deposit}\n5.Rent(per day): {Audi_A5_Rent}")
                rent = input("Do you want to rent this model:- ")
                if rent == "yes" or "Yes" or "YES" or "Y" or "y":
                    rentday = int(input("How many days do you want to rent the car:- "))
                    print(f"\tDelux Motor Pvt Ltd\n\tPune\nName:- {name}\nAge:- {age}\nLicense:- Yes\nRented Car:- Audi A5\nNo of Day to be rented:-{rentday}\nBase Payment:- {Audi_A5_Rent*rentday}\nDeposit:- {Audi_A5_Deposit}\nTotal Payable amount:- {Audi_A5_Deposit+(Audi_A5_Rent*rentday)}")
            elif car==3:
                print(f"Audi TT Details:\n1.Comapany: Audi\n2.Type: Luxury Sedan\n3.Mileage: 14KMPL\n4.Deposit: {Audi_TT_Deposit}\n5.Rent(per day): {Audi_TT_Rent}")
                rent = input("Do you want to rent this model:- ")
                if rent == "yes" or "Yes" or "YES" or "Y" or "y":
                    rentday = int(input("How many days do you want to rent the car:- "))
                    print(f"\tDelux Motor Pvt Ltd\n\tPune\nName:- {name}\nAge:- {age}\nLicense:- Yes\nRented Car:- Audi TT\nNo of Day to be rented:-{rentday}\nBase Payment:- {Audi_TT_Rent*rentday}\nDeposit:- {Audi_TT_Deposit}\nTotal Payable amount:- {Audi_TT_Deposit+(Audi_TT_Rent*rentday)}")
            again = input("Do you want to continue with the selected card")