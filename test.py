import numpy as np
import pandas as pd
prediction = {
    "a_count" : [],
    "b_count" : [],
    "c_count" : [],
    "d_count" : [],
    "e_count": [],
    "f_count" : []
}

l1 = []
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n=0
for i in range(36):
    a = np.random.choice([1, 2, 3, 4, 5, 6])
    l1.append(int(a))

    if a == 1:
        
        prediction["a_count"].append(n+1)
        n1=+1
    elif a == 2:
        prediction["b_count"].append(n+1)
        n2=+1
    elif a == 3:
        prediction["c_count"].append(n+1)
        n3=+1
    elif a == 4:
        prediction["d_count"].append(n+1)
        n4=+1
    elif a == 5:
        prediction["e_count"].append(n+1)
        n5=+1
    elif a == 6:
        prediction["f_count"].append(n+1)
        n6=+1

print("1 appeared:", n1)
print("2 appeared:", n2)
print("3 appeared:", n3)
print("4 appeared:", n4)
print("5 appeared:", n5)
print("6 appeared:", n6)

data = pd.date_range(l1)
n=1
data.to_csv("/run/media/yash-tupe/Local Disk E/Linux/Sumago Python/Data.csv",index=False)