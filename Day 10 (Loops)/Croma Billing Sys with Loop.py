#Welcome to electronic shop
#Ask name then display the price of and 5 products
#Which product user want to buy , which product and quantity do you want to buy something else
print("\t Welcome to the Croma retail Store")
name = input("Enter your name: ")

Mobile = 9999
Laptop = 50000
Oven = 6999
Ac = 30000
Fridge = 15000
print(f"Welcome {name}")
want_to_purchase = input("Do you want to view the list of product available: ")
if want_to_purchase == "yes" or "Yes" or "Y" or "y":
    print(f"Available Product at our store\n1.Mobile Price = {Mobile}\n2.Laptop Price = {Laptop}\n3.Oven Price = {Oven}\n4.AC Price = {Ac}\n5.Fridge Price = {Fridge}")
    while want_to_purchase == "yes" or "Yes" or "Y" or "y":
        choice = int(input("Enter the serial no of the product you want"))
        if choice==1:
            print(f"Your selected no product is Mobile\nPrice = {Mobile}")
            qty = int(input("Enter the quantity: "))
            print(f"Bill to be paid\nProduct Selected - Mobile\nQuantity - {qty}\nTotal payable amount {qty*Mobile}")
        elif choice==2:
            print(f"Your selected no product is Laptop\nPrice = {Laptop}")
            qty = int(input("Enter the quantity: "))
            print(f"Bill to be paid\nProduct Selected - Laptop\nQuantity - {qty}\nTotal payable amount {qty*Laptop}")
        elif choice==3:
            print(f"Your selected no product is Oven\nPrice = {Oven}")
            qty = int(input("Enter the quantity: "))
            print(f"\tThank you {name} for trusting us.\nBill to be paid\nProduct Selected - Oven\nQuantity - {qty}\nTotal payable amount {qty*Oven}")
        elif choice==4:
            print(f"Your selected no product is Ac\nPrice = {Ac}")
            qty = int(input("Enter the quantity: "))
            print(f"Bill to be paid\nProduct Selected - Ac\nQuantity - {qty}\nTotal payable amount {qty*Ac}")
        elif choice==5:
            print(f"Your selected no product is Fridge\nPrice = {Fridge}")
            qty = int(input("Enter the quantity: "))
            print(f"Bill to be paid\nProduct Selected - Fridge\nQuantity - {qty}\nTotal payable amount {qty*Fridge}")
        want_to_purchase = input("Do you want Buy another ")
else:
    print("Sorry that we don't have the product you want")