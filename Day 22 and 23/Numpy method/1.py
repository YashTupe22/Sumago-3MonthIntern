#Numpy stand for numerical python
#Generally used for numerical python
#it is faster than list 
#used for working with array
import numpy as np
arr1 = np.array([[10,20,30],[40,50,60]])
print(arr1)
print(arr1+1)
print(arr1-1)
print(arr1*2)
print(arr1/2)
print(arr1.min())
print(arr1.max())
print(arr1.sum())
print(arr1.cumsum())
print(arr1.cumprod())
arr2 = np.array([[10,20,30],[40,50,60]])
print(np.size(arr1))
print(np.append(arr1,arr2))
print(f"Vertical {np.vstack(arr1)}")
print(f"Horizontal {np.hstack(arr1)}")
print(np.ndim(arr1))
n = np.average(arr1)
print(n)
print(np.unique(arr1))
print(np.sort(arr1,reversed))
