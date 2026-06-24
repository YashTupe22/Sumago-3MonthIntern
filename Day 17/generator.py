def generator():
    i = 259
    while i <=200:
        yield 1
        print(i)
        i+=1
x=generator()
print(x)
print(x)