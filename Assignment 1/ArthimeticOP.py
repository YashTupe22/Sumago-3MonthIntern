# Arithmetic Operators
# 1. Simple Calculator - Perform addition, subtraction, multiplication, division, modulus, and exponent operations on two numbers.
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print(f"Addition: {a+b}\nSubstraction: {b-a}\nMultiplication: {a*b}\nDivison: {a/b}\nModulus: {a//b}\nExpontential: {a**b}")

# 2. Student Marks Calculation - Calculate total, average, and percentage of student marks.
marks1 =int(input("Enter Marks 1:"))
marks2 =int(input("Enter Marks 2:"))
marks3 =int(input("Enter Marks 3:"))
total = marks1+marks2+marks3
print(f"Total of marks is {total}")
avg = (marks1+marks2+marks3)/3
print(f"Average of marks {avg}")
per = (marks1+marks2+marks3)*100/300
print(f"Percentage student achieve {per}%")
# 3. Salary Calculation System - Calculate gross salary, deductions, and net salary.
print("\tWelcome to Salary Calculation System")
print("Please enter mention details or amount related to your salary")
print("\tWelcome to Salary Calculation System")
#Gross Salary = Basic Salary + HRA + Allowances + Bonuses + Overtime
bs = int(input("Enter your Basic Salary:- "))
hra = int(input("Enter your HRA:- "))
allowance = int(input("Enter your allowance amount:- "))
bonus = int(input("Enter your bonus amount:- "))
#total Deductions = PF + Professional Tax + Income Tax + Insurance 
pf = int(input("Enter your deducted pf amount:- "))
it = int(input("Enter your deducted Income tax amount:- "))
insurance = int(input("Enter your deducted Insurance amount:- "))
Gross_salary = bs+hra+allowance+bonus
deduction = pf+it+insurance
print(f"Detailed Salary analysis\n1)Gross Salary: {Gross_salary}\n2)Deduction: {deduction}\n3)Net salary: {Gross_salary-deduction} ")
# 4. Shopping Bill Calculator - Calculate total bill amount based on product prices and quantities.
no = int(input("Enter the no of product purchased: "))
totalbill = 0
for i in range(1,no+1):
    print(f"Product {i}")
    name = (input("Enter the product name: "))
    price = int(input("Enter the product price: "))
    quantites = int(input("Enter the product quantity: "))
    cost = price*quantites
    totalbill += cost
    print(f"Prpduct Cost {cost}")

print(f"Total bill for your shopping bill is {totalbill}")
# 5. Electricity Bill Calculation - Calculate electricity charges based on units consumed.
print("\tElectricity Bill Calculation")
perunit = 13
unitused = int(input("Enter the no unit used: "))
bill = unitused*perunit
print(f"The Electrcity bill for you at {unitused} units is {bill}")