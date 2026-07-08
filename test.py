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
print("Numeric columns: \n", numeric_cols)
print("Categorical columns: \n", categorical_cols)
print("Datetime columns: \n", datetime_cols)
print(df.nunique().sort_values(ascending=False))

missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_table = pd.DataFrame({
"MissingCount": missing,
"MissingPercent": missing_pct
}).sort_values("MissingCount", ascending=False)
# Show only columns that actually have missing values.
print(missing_table[missing_table.MissingCount > 0])
mt = missing_table[missing_table.MissingCount > 0]
plt.figure(figsize=(8, 4))
plt.bar(mt.index, mt.MissingPercent, color='RED', edgecolor="#9E0C24")
plt.title("Missing Values by Column (%)")
plt.ylabel("Missing %")
plt.xticks(rotation=20)
for i, v in enumerate(mt.MissingPercent):
# annotate each bar
    plt.text(i, v + 0.1, f"{v}%", ha="center", fontsize=9)
plt.tight_layout()
plt.show()

# --- 7.2 (cont.) missingno: matrix + heatmap of missingness patterns ---
# The matrix shows WHERE values are missing; the heatmap shows whether
# missingness in one column CORRELATES with another (nullity correlation).

if np.HAS_MSNO:
    np.msno.matrix(df, color=(0.78, 0.06, 0.18))
    plt.title("Missingno Matrix - location of missing values")
    plt.show()
    np.msno.heatmap(df)
    plt.title("Missingno Heatmap - nullity correlation")
    plt.show()
else:
    print("missingno not available - showing pandas-based pattern instead.")
    np.sns.heatmap(df.isnull(), cbar=False, cmap="Reds")
    plt.title("Missing Value Map (yellow/red = missing)")
    plt.show()