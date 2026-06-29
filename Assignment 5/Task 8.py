# Create an array and find the sum and average of all elements.
import numpy as np
a = np.array([10,20,30,40,50,60])
print(f"Sum of array: {a.sum()}")
print(f"Average of Array: {a.sum()/a.size}")
print(f"Average of Array using np.average(): {np.average(a)}")