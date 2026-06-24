#Student Marks Analyzer
#Calculate total,average, highes, lowest makrs and count students above a threshold

n = int(input("How many students marks are needed to be analyzed: "))


for n in range(1,n+1):
    print("\tStudent Marks Analysis Panel")
    name = input("Enter the Student Name: ")
    m1 = int(input("Enter the Marks for Subject 1: "))
    m2 = int(input("Enter the Marks for Subject 2: "))
    m3 = int(input("Enter the Marks for Subject 3: "))
    print("\tReport")
    print(f"Name: - {name}")
    total = m1+m2+m3
    print(f"Total Marks: - {total}")
    average = total/3
    print(f"Average Marks Scored: - {average}")
    a = max(m1,m2,m3)
    print(f"Highest Marks obtained: - {a}")
    b = min(m1,m2,m3)
    print(f"Lowest Marks obtained: - {b}")
    i = 0
    if total >= 200:
        print("Above the Threshold")
