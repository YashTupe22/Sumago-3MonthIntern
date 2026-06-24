def con(f):
    def wrapper():
        print("Before")
        f()
        print("After")
    return wrapper
def hello():
    print("Hello")
go = con(hello())