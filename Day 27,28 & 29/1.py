import pandas as pd
import numpy as np
a = pd.read_csv("/home/yash-tupe/Downloads/1-1.csv")
print(a)
print(a.head())
print(a.head(3))
print(a.tail())
print(a.tail(3))

print(a.isna())
print(a.isnull())
print(a.isnull().sum())
print(a.isnull().sum().sum())
print(a.isnull().any())
print(a.isnull().any().any())

print(a.fillna(0))
print(a.isna())
