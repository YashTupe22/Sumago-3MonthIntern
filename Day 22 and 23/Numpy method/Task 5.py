import numpy as np
a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
b=a.reshape(9)
c = np.flatten(a)
print(b)
print(c)
print(np.ndim(a))
print(np.shape(a))
print(np.shape(a))