import numpy as np
a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
print(a.flatten())
print(a.ravel())
a1 = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
b1 = np.array([[30,20,10],
              [60,50,40],
              [90,80,70]])

print(f"Addition \n{np.add(a1,b1)}")
print(f"Substraction \n{np.subtract(a1,b1)}")
print(f"Multiplication \n{np.multiply(a1,b1)}")
print(f"Division \n{np.divide(a1,b1)}")
print(f"Square root \n{np.sqrt(a1)}")
print(f"Pow \n{np.pow(a1,2)}")

print(f"Maximum in array {np.argmax(a)}")
print(f"Minimium in array {np.argmin(a)}")

print(f"Transpose \n{np.transpose(a)}")
print(np.where(a>50))

print(f"Random no between 1-20: {np.random.randint(1,20)}")
print(f"Random Choice from array A: {np.random.choice([1,4,6,7,8,5,3,1])}")
print(f"Standard Deviation: {np.std(a)}")
print(f"Varience: {np.var(a)}")
print(f"Unique: {np.unique(a)}")