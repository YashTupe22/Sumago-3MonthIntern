# Logical Operators(also use conditional statements)
# 1. Loan Eligibility Checker
cibil = int(input("Enter your Cibil score: "))
loan = int(input("No of loan taken: "))
if(cibil>=750 or loan >= 3):
    print("You are eligible of loan")
else:
    print("Your are not eligible")
# 2. Voting Eligibility Verification
age = int(input("Enter you age: "))
if(age >= 18):
    print("You are eligible to vote")
else:
    print("Your are not eligible")
# 3. Employee Bonus Eligibility

ot = int(input("Enter your Overtime hours"))
if(ot>3):
    print("You are eligible for the Bonus")
else:
    print("Your are not eligible")
# 4. Admission Eligibility Check

per = float(input("Enter your percentage: "))
if(per >= 80):
    print("Your are eligible for admission in our college")

else:
    print("You are not eligible for the admission in our college")
# 5. Scholarship Eligibility Verification
income = int(input("Enter you parent's Annual: "))
if(income < 200000):
    print("Eligible for the scholarship")
else:
    print("Not eligible for scholarship")