print("\tWelcome to XYZ login")
login_attempt = 3
n=1
while login_attempt > 0:
    
    id = input("Enter your userid: ")
    pin = int(input("Enter you pin: "))
    if pin == 2224:
        print("Login Successful")
        login_attempt == 0
        break
    else:
        login_attempt -=1
        continue
    login_attempt = n
