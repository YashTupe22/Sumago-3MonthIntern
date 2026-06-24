def Audi():
    
    print("\tWelcome to Deluxe Car Rental Service")

name = input("Please enter your name:- ")
age = int(input("Enter your Age:- "))

if age >=18:
    print(f"Hey Mr.{name}, you are partially eligible to rent out a Car🥳!!")
    license = input("Do you have a valid license:- ")
    if license == "yes" or "Yes" or "YES" or "y" or "Y":
        pass
else:  

    print("You are not eligible for the renting out the car because you are under age!! Sorry")