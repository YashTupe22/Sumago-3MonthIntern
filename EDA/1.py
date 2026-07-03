import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
data = pd.read_csv("/run/media/yash-tupe/Local Disk E/Linux/Sumago Python/EDA/Amazon Sale Report.csv")
print(data.head())
print(data.tail())
print(data.describe())
x = data[1]