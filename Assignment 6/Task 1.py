import pandas as pd
import numpy as np
# 1. Create a Series of monthly temperatures: [22, 25, 28, 32, 35, 33, 30, 28, 26, 23, 20, 18]
# # with index as month names ['Jan', 'Feb', ..., 'Dec']
temperatures = [22,25,28,32,35,33,30,28,26,23,20,18]
index = ["Jan",'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
temperatures = pd.Series(temperatures,index=index)
print(temperatures)
# 2. Find the hottest and coldest months
hot = temperatures[temperatures==temperatures.max()]
print("Hottest Month ",hot)
cold = temperatures[temperatures==temperatures.min()]
print("Hottest Month ",cold)
# 3. Calculate the average temperature
avg = temperatures.sum()/temperatures.size
print("Avwerage temperature ",avg)
# 4. Find months with temperature above 25°C
print(temperatures[temperatures>25])
# 5. Create a new Series with temperature in Fahrenheit (F = C * 9/5 + 32)
new_temp = []
for i in range(0,len(temperatures)):
    F = temperatures.iloc[i]*9/5+32
    new_temp.append(F)
    i+=1
new_temp = pd.Series(new_temp)
print(new_temp)