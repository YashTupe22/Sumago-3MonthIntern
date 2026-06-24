p1 = "Harry Potter"
p2 = "Rich Dad Poor Data"
p3 = "Atomic Habit"
p4 = "Basic of Python"
p5 = "DSA practice"
print("\tLibrary MANAGEMENT SYSTEM")
while True:
    print("\tMain Menu")
    print("1. View Book")
    print("2. Search Books")
    print("3. Borrow Book")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n--- Book List ---")

        for i in range(1, 6):
            if i == 1:
                Book = p1
            elif i == 2:
                Book = p2
            elif i == 3:
                Book = p3
            elif i == 4:
                Book = p4
            else:
                Book = p5

            if Book == "":
                continue

            print(f"Book {i}: {Book}")

    elif choice == 2:
        search = input("Enter Book name to search: ")
        found = 0

        for i in range(1, 6):

            if i == 1:
                Book = p1
            elif i == 2:
                Book = p2
            elif i == 3:
                Book = p3
            elif i == 4:
                Book = p4
            else:
                Book = p5
          
            if Book.lower() == search.lower():
                print("Book Found!")
                print("Position:", i)
                found = 1
                break

        if not found:
            print("Book Not Found!")


    elif choice == 3:
        Borrow = input("Which book do you want to borrow")
        Available = 0

        for i in range(1, 6):

            if i == 1:
                Book = p1
            elif i == 2:
                Book = p2
            elif i == 3:
                Book = p3
            elif i == 4:
                Book = p4
            else:
                Book = p5
          
            if Book.lower() == Borrow.lower():
                print("Book Borrowed Successfully!")
                print("Position:", i)
                Book = ""
                Available = 1
                break

        if not Available:
            print("Book Already borrowed!")
    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")