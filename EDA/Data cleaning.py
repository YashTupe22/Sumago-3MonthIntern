import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import warnings
df = pd.read_csv("/run/media/yash-tupe/Local Disk E/Linux/Sumago Python/EDA/CSV/Amazon Sale Report.csv")
print(df.head())
print(df.tail())
print(np.shape(df))
print(df.describe())

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(include="object").columns.tolist()
datetime_cols = df.select_dtypes(include="datetime").columns.tolist()
print("Numeric columns:", numeric_cols)
print("Categorical columns:", categorical_cols)
print("Datetime columns:", datetime_cols)

print("No of Null value in Amount ",df['Order ID'].isna().sum())
print(df['Order ID'].duplicated())
df.update(df['Order ID'].drop_duplicates())
print(df['Order ID'])

print("No of Null value in Currency ",df['currency'].isna().sum())
print(df['currency'].isna().sum())
df.update(df['currency'].fillna("INR"))
print(df['currency'])

print("No of Null value in Amount ",df['Amount'].isna().sum())
df.update(df['Amount'].fillna(df['Amount'].mean('index')))
print(df['Amount'])
print(df['Amount'].isna().sum())

print("No of Null value in Promotional id ",df['promotion-ids'].isna().sum())
df.update(df['promotion-ids'].fillna('UNK'))
print(df['promotion-ids'])
print(df['promotion-ids'].isna().sum())

print("No of Null value in Courier Status ",df['Courier Status'].isna().sum())
df.update(df['Courier Status'].fillna('Not Updated'))
print(df['Courier Status'])
print(df['Courier Status'].isna().sum())

print("No of Null value in fulfilled-by ",df['fulfilled-by'].isna().sum())
df.update(df['fulfilled-by'].fillna(0))
print(df['fulfilled-by'])
print(df['fulfilled-by'].isna().sum())
print(df.isna().sum())

df.to_csv("/run/media/yash-tupe/Local Disk E/Linux/Sumago Python/EDA/CSV/Amazon Sale Report updated.csv")


