import pandas as pd
import numpy as np

d1 = pd.Series([1,2,3,4,5])
print(d1)

d2 = pd.Series([1,2,3,4,5],index=["A","B","C","D","E"])
print(d2)

data = {
    "Name":['Alice','Bob','Charile','Diana'],
    "Age":[25,30,40,28],
    'City':['New York','London','Tokyo','Paris'],
    'Salary':[50000,60000,70000,55000]
}

df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data,index=[1,2,3,4])
print(df)

df2 = [{"Name":"Alice","Age":28,"City":"New York","Salary":60000},
       {"Name":"Charile","Age":38,"City":"Delhi","Salary":55000}]
df2 = pd.DataFrame(df2)
print(df2)

# Select Single Row
print(df.loc[1])

# Select Multiple Row
print(df.loc[1:2])

# Selected Rows and columns
print(df.loc[1:3,"Name":"City"])

# Selected by position
print(df.iloc[0])

# Select non-consecutive position
print(df.iloc[[0,2],[0,2]])

a = df[df["Age"]<30]
print(a)

a = df[(df["Age"]<30) & (df["Salary"]<70000)] 
print(a)

b = df[df['Name'].isin(["Alice"])]
print(b)

