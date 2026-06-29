import numpy as np

a_count = 0
b_count = 0
c_count = 0
d_count = 0
e_count = 0
f_count = 0

l1 = []

for i in range(36):
    a = np.random.choice([1, 2, 3, 4, 5, 6])
    l1.append(int(a))

    if a == 1:
        a_count += 1
    elif a == 2:
        b_count += 1
    elif a == 3:
        c_count += 1
    elif a == 4:
        d_count += 1
    elif a == 5:
        e_count += 1
    elif a == 6:
        f_count += 1

print("1 appeared:", a_count)
print("2 appeared:", b_count)
print("3 appeared:", c_count)
print("4 appeared:", d_count)
print("5 appeared:", e_count)
print("6 appeared:", f_count)

print("Total rolls:", len(l1))
print("Rolls:", l1)