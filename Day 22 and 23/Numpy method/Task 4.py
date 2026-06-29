import numpy as np
sales = np.array([5000,7500,8700,5400,6565,7034,7565,9043,5786,8065])
print(f"Sum of sales: {np.sum(sales)}")
print(f"Mean of sales: {np.mean(sales)}")
print(f"Max of sales: {np.max(sales)}")
print(f"Min of sales: {np.min(sales)}")
print(f"Sales are less than 7000: {np.where(sales >=7000)}")