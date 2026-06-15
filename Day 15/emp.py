def emp():
    Emp_db = {"Name":["Yash"],
              "Salary:":[10000],
              "Add":["Pune"],
              "Des":["Engg"]
              }
    print(Emp_db)
    
    while True:
        print("Choose any of the one feature you want to use\n1.Add\n2.Search\n3.Remove\n4.View")
        choose = int(input())
        if choose == 1:
            Name = input("Enter your name:- ")
            Salary = int(input("Enter your Salary:- "))
            Add = input("Enter your Office Location:- ")
            Des = input("Enter your designation:- ")
            Emp_db["Name"].append(Name)
            Emp_db["Salary:"].append(Salary)
            Emp_db["Add"].append(Add)
            Emp_db["Des"].append(Des)
            print(f"Added Succuessfully\n{Emp_db}")
        elif choose == 2:
            Name = input("Enter your name:- ")  
            for i in range(0,len(Emp_db)-1):
                if Name in Emp_db["Name"]:
                    print("Found in the Database")
                    break
                else:
                    print("Not found")
        elif choose == 3:
            Name = input("Enter the Name you want to remove:- ")
            Emp_db.popitem(Name)
        elif choose == 4:
            print(Emp_db)

emp()