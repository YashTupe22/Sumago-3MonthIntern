print("\tWelcome to Deluxe Car Rental Service")

name = input("Please enter your name:- ")
age = int(input("Enter your Age:- "))

if age >=18:
    print(f"Hey Mr.{name}, you are partially eligible to rent out a Car🥳!!")
    license = input("Do you have a valid license:- ")
    if license == "yes" or "Yes" or "YES" or "y" or "Y":
        print(f"Mr. {name}, you can rent out a car from our service.\nCurrently we have Three Premium Car company lineup\n1. Audi\n2. BMW\n3.Mercedes Benz")
        company = int(input("Enter the serial no of your prefered car company:- "))
        if company == 1:
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
        if company == 2:
            BMW_x7_Deposit = 80000
            BMW_x7_Rent = 40000

            BMW_M340I_Deposit = 120000
            BMW_M340I_Rent = 75000

            BMW_7_Deposit = 250000
            BMW_7_Rent = 150000

            print(f"Mr. {name} for BMW. We currently provide 3 best model of them for renting out\nModels:-\n1.BMW x7\n2.BMW M340i\n3.BMW 7 series")
            again = "No"

            while again == "no" or "No" or "N" or "n":
                car = int(input("Enter the serial no of selected model for futher detail:- "))
                if car==1:
                    print(f"BMW x7 Details:\n1.Comapany: BMW\n2.Type: SUV\n3.Mileage: 14KMPL\n4.Deposit: {BMW_x7_Deposit}\n5.Rent(per day): {BMW_x7_Rent}")
                    rent = input("Do you want to rent this model:- ")
                    if rent == "yes" or "Yes" or "YES" or "Y" or "y":
                        rentday = int(input("How many days do you want to rent the car:- "))
                        print(f"\tDelux Motor Pvt Ltd\n\tPune\nName:- {name}\nAge:- {age}\nLicense:- Yes\nRented Car:- BMW x7\nNo of Day to be rented:-{rentday}\nBase Payment:- {BMW_x7_Rent*rentday}\nDeposit:- {BMW_x7_Deposit}\nTotal Payable amount:- {BMW_x7_Deposit+(BMW_x7_Rent*rentday)}")
                elif car==2:
                    print(f"BMW M340i Details:\n1.Comapany: BMW\n2.Type: Sedan\n3.Mileage: 14KMPL\n4.Deposit: {BMW_M340I_Deposit}\n5.Rent(per day): {BMW_M340I_Rent}")
                    rent = input("Do you want to rent this model:- ")
                    if rent == "yes" or "Yes" or "YES" or "Y" or "y":
                        rentday = int(input("How many days do you want to rent the car:- "))
                        print(f"\tDelux Motor Pvt Ltd\n\tPune\nName:- {name}\nAge:- {age}\nLicense:- Yes\nRented Car:- BMW M340i\nNo of Day to be rented:-{rentday}\nBase Payment:- {BMW_M340I_Rent*rentday}\nDeposit:- {BMW_M340I_Deposit}\nTotal Payable amount:- {BMW_M340I_Deposit+(BMW_M340I_Rent*rentday)}")
                elif car==3:
                    print(f"BMW 7 Series Details:\n1.Comapany: BMW\n2.Type: Luxury Sedan\n3.Mileage: 14KMPL\n4.Deposit: {BMW_7_Deposit}\n5.Rent(per day): {BMW_7_Rent}")
                    rent = input("Do you want to rent this model:- ")
                    if rent == "yes" or "Yes" or "YES" or "Y" or "y":
                        rentday = int(input("How many days do you want to rent the car:- "))
                        print(f"\tDelux Motor Pvt Ltd\n\tPune\nName:- {name}\nAge:- {age}\nLicense:- Yes\nRented Car:- BMW 7 Series\nNo of Day to be rented:-{rentday}\nBase Payment:- {BMW_7_Rent*rentday}\nDeposit:- {BMW_7_Deposit}\nTotal Payable amount:- {BMW_7_Deposit+(BMW_7_Rent*rentday)}")
                again = input("Do you want to continue with the selected card")      
        if company == 3:
            MB_GLA200_Deposit = 80000
            MB_GLA200_Rent = 40000

            MB_CLA_Deposit = 120000
            MB_CLA_Rent = 75000

            MB_S_Deposit = 250000
            MB_S_Rent = 150000

            print(f"Mr. {name} for Mercedes Benz. We currently provide 3 best model of them for renting out\nModels:-\n1.Mercedes Benz GLA200\n2.Mercedes Benz CLA\n3.Mercedes Benz S200")
            
            again = "No"

            while again == "no" or "No" or "N" or "n":
                car = int(input("Enter the serial no of selected model for futher detail:- "))
                if car==1:
                    print(f"Mercedes Benz GLA200 Details:\n1.Comapany: Mercedes Benz\n2.Type: SUV\n3.Mileage: 14KMPL\n4.Deposit: {MB_GLA200_Deposit}\n5.Rent(per day): {MB_GLA200_Rent}")
                    rent = input("Do you want to rent this model:- ")
                    if rent == "yes" or "Yes" or "YES" or "Y" or "y":
                        rentday = int(input("How many days do you want to rent the car:- "))
                        print(f"\tDelux Motor Pvt Ltd\n\tPune\nName:- {name}\nAge:- {age}\nLicense:- Yes\nRented Car:- Mercedes Benz GLA200\nNo of Day to be rented:-{rentday}\nBase Payment:- {MB_GLA200_Rent*rentday}\nDeposit:- {MB_GLA200_Deposit}\nTotal Payable amount:- {MB_GLA200_Deposit+(MB_GLA200_Rent*rentday)}")
                elif car==2:
                    print(f"Mercedes Benz CLA Details:\n1.Comapany: Mercedes Benz\n2.Type: SUV\n3.Mileage: 14KMPL\n4.Deposit: {MB_CLA_Deposit}\n5.Rent(per day): {MB_CLA_Rent}")
                    rent = input("Do you want to rent this model:- ")
                    if rent == "yes" or "Yes" or "YES" or "Y" or "y":
                        rentday = int(input("How many days do you want to rent the car:- "))
                        print(f"\tDelux Motor Pvt Ltd\n\tPune\nName:- {name}\nAge:- {age}\nLicense:- Yes\nRented Car:- Mercedes Benz CLA\nNo of Day to be rented:-{rentday}\nBase Payment:- {MB_CLA_Rent*rentday}\nDeposit:- {MB_CLA_Deposit}\nTotal Payable amount:- {MB_CLA_Deposit+(MB_CLA_Rent*rentday)}")
                elif car==3:
                    print(f"Mercedes Benz S200 Details:\n1.Comapany: Mercedes Benz\n2.Type: Luxury Sedan\n3.Mileage: 14KMPL\n4.Deposit: {MB_S_Deposit}\n5.Rent(per day): {MB_S_Rent}")
                    rent = input("Do you want to rent this model:- ")
                    if rent == "yes" or "Yes" or "YES" or "Y" or "y":
                        rentday = int(input("How many days do you want to rent the car:- "))
                        print(f"\tDelux Motor Pvt Ltd\n\tPune\nName:- {name}\nAge:- {age}\nLicense:- Yes\nRented Car:- Mercedes Benz S200\nNo of Day to be rented:-{rentday}\nBase Payment:- {MB_S_Rent*rentday}\nDeposit:- {MB_S_Deposit}\nTotal Payable amount:- {MB_S_Deposit+(MB_S_Rent*rentday)}")
                again = input("Do you want to continue with the selected card")
else:  

    print("You are not eligible for the renting out the car because you are under age!! Sorry")