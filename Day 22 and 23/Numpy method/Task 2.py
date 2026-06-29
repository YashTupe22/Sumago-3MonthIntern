import numpy as np
sal = np.array([5000,7500,8700,5400,6565,7034,7565,9043,5786,8065])
sal=sal+500
print(f"Updated salary with bonus {sal}")
print(f"Total salary: {np.sum(sal)}")
print(f"Average salary: {np.average(sal)}")
print(f"Highest salary: {np.max(sal)}")
print(f"Lowest salary: {np.min(sal)}")