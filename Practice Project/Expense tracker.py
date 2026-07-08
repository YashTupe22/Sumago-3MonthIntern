'''Expense Tracker
Requirements
Features
Add expenses separated by commas
Calculate:
total expense
highest expense
lowest expense
average expense
lists
split()
loops
type conversion
arithmetic
max()
min()
sum()
'''
print("\t-----Welcome to the Expense tracker-----")
get = input("Enter the expenses separated by commas:- ")
b = get.split(",")
a = list(b)
count=0
a1=[]
for i in range(0,len(a)):
    conv = int(a[i])
    a1.append(conv)
    count+=1

#For showing use there expense
count1 = 1
for i in range(0,len(a1)):
    print("Expense no",count1,"- ",a[i])
    count1+=1
print("Expense Report- ")
print("Total expense-",sum(a1))
print("Maximum Expense -",max(a1))
print("Minimuim Expense -",min(a1))
print("Average Expense",(sum(a1)//len(a1)))


