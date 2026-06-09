#If statement
age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote")

#If - else statement
age = int(input("Enter your age: "))
voter_id = input("Do you have voter id: ")
if age>=18 and voter_id =="Yes" or "y" or "Yes" or "Y" :
    print("You are eligible to vote")
else:
    print("you are not eligible to vote")

#Nested IF statement
age = int(input("Enter your age: "))
if age>=18 :
    print("You are eligible to vote")
    voter_id = input("Do you have voter id: ")
    if voter_id =="Yes" or "y" or "Yes" or "Y":
        print("Your are eligible to vote because you have the voter id")
else:
    print("you are not eligible to vote")

#Elif statement
age = int(input("Enter your age: "))
voter_id = input("Do you have voter id: ")
if age>=18 :
    print("You are eligible to vote")
elif voter_id =="Yes" or "y" or "Yes" or "Y":
    print("Your are eligible to vote because you have the voter id")
else:
    print("you are not eligible to vote")