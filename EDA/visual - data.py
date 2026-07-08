import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("/run/media/yash-tupe/Local Disk E/Linux/Sumago Python/EDA/CSV/Amazon Sale Report updated.csv")

x = data['Amount'].head(5)
y = data['Category'].head(5)
print(y)
plt.bar(x)
plt.show()