# Create a simple banking application where the user can:

# check Database
# deposit money
# withdraw money
# exit system
print("\tWelcome to Alibaba ki Tijori Bank")

print("\n\t1.Login up(Already User)" \
"\n\t2.Sign up(New User)")

ls = int(input("Enter your choose(*Option no)-"))
log_out = 0
#Database
Database = {
    1 : 5000,
    2 : 7000,
    3 : 9000,
    4 : 10000,
    5 : 12000
}
choose = 0
if ls ==1:
    acc_no = int(input("Welcome Back," \
    "\n\tEnter Account no- "))
    if acc_no in Database:
        
        print("\nWelcome back Sir/Madam" \
        "\n1)Check Database" \
        "\n2)Deposit Money" \
        "\n3)Withdraw Money" \
        "\n4)Exit")
        choose = int(input("Enter your choice- "))
    else:
        print("\nSorry Wrong Account No")
    a = acc_no
    choose_Logout = 4
    while choose_Logout == 4:
        if choose == 1: 
            print("Your Database- ",Database[a])
        elif choose == 2:
            deposit = int(input("Enter the amount to be desposit- "))
            Database[a]=Database[a]+deposit
            print("Bank Database after deposit-",Database[a])
        elif choose ==3:
            withdraw = int(input("Enter the amount to be withdrawn- "))
            if Database[a] <=withdraw:
                print("Database is insufficient")
            else:
                Database[a]=Database[a]-withdraw
                print("Amount is withdrawn successfully\nBank Database after withdrawl",Database)
        elif choose ==4:
            print("Thank you choosing Ali baba ki tijori bank" \
            "   \n\tLogout Successfully")
        
elif ls == 2:
    print("Welcome Create your account no")
    acc_no = int(input("Enter Account No you want - "))
    if(acc_no in Database):
        print("Account no already exists, please try again")
    else:
        Database[acc_no] = [0]
        add_Database = int(input("Add money to your account- "))
        
        Database[acc_no]=(add_Database)
        print("Your account has been created")
        print("\nWelcome back Sir/Madam" \
        "\n1)Check Database" \
        "\n2)Deposit Money" \
        "\n3)Withdraw Money" \
        "\n4)Exit")
        choose = int(input("Enter your choice- ")) 

else:
    print("Entered the wrong choice")

        


    

