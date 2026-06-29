import numpy as np
a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
for i in range(0,len(a)):
    if a.any()>= 50:
        print(a[i])
