def vote():
    name = input("Enter your name:- ")
    print(f"Name:- {name}")
    age = int(input("Enter your age:- "))
    if age >=18:
        print("Your are eligible to vote")
    else:
        print("You are not eligible")
vote()