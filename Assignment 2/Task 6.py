p1 = ""
p2 = ""
p3 = ""
p4 = ""
p5 = ""
print("\tINVENTORY MANAGEMENT SYSTEM")
while True:
    print("\tMain Menu")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        product = input("Enter product name: ")
        if p1 == "":
            p1 = product
            print("Product added successfully.")
        elif p2 == "":
            p2 = product
            print("Product added successfully.")
        elif p3 == "":
            p3 = product
            print("Product added successfully.")
        elif p4 == "":
            p4 = product
            print("Product added successfully.")
        elif p5 == "":
            p5 = product
            print("Product added successfully.")
        else:
            print("Inventory Full!")

    elif choice == 2:
        print("\n--- Product List ---")

        for i in range(1, 6):
            if i == 1:
                product = p1
            elif i == 2:
                product = p2
            elif i == 3:
                product = p3
            elif i == 4:
                product = p4
            else:
                product = p5

            if product == "":
                continue

            print(f"Product {i}: {product}")

    elif choice == 3:
        search = input("Enter product name to search: ")
        found = 0

        for i in range(1, 6):

            if i == 1:
                product = p1
            elif i == 2:
                product = p2
            elif i == 3:
                product = p3
            elif i == 4:
                product = p4
            else:
                product = p5
          
            if product.lower() == search.lower():
                print("Product Found!")
                print("Position:", i)
                found = 1
                break

        if not found:
            print("Product Not Found!")

    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")