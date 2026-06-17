def display(f):
    def wrapper(num):
        print("Logs")
        result = f(num)
        primes = list(result)
        print(primes)
        return primes
    return wrapper

@display
def genprime(n):
    for num in range(2, n):
        is_prime = True
        for i in range(2,int(num**0.5)+1):
            if num %i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

x=genprime(50)