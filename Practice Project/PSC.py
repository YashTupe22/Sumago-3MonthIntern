# 2. Password Strength Checker

# Concepts used: strings, operators, conditions

# Check:

# Length = 8
# Uppercase = 3
# Numbers = yes
# Special characters = 3

# Example output:

# Strong Password
# Weak Password

# This project improves logical thinking massively.
print("----- Welcome to password Checker-----")
password = input("Enter your password- ")
count = 0
num = False
special = False
for char in password:
        if char.isupper():
            count+=1
        if char.isdigit():
            num = True
        if not  char.isalnum():
             special = True
             
if len(password) >= 8 and count <=1 and special and num:
    print("Your Password is Strong")
else:
     print("Your password  is weak")
                