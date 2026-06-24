def bank(f):
    def wrapper(balance,amount):
        print("Logs")
        print(f"Balance: {balance}")
        print(f"Amount: {amount}")
        new_balance = f(balance,amount)
        print(f"New Balance: {new_balance}")
        return new_balance
    return wrapper

@bank
def deposit(balance,amount):
    balance += amount
    return balance

@bank
def withdraw(balance,amount):
    if balance<amount:
        print("Insufficient Balance")
        
    balance -= amount
    return balance
balance = 1000
balance = deposit(balance,500)
balance = withdraw(balance,100)