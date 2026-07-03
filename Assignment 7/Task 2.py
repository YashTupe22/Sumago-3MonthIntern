import pandas as pd
import numpy as np
# 12.Time Series Data Combination
# Objective: Work with temporal data merging
# Tasks: 
# 1. Combine all stock prices into a single DataFrame 
stock_set1 = pd.DataFrame({
    "Date": ["2025-01-01", "2025-01-02", "2025-01-03"],
    'Wipro':[5012,5025,5075],
    'GOOGl':[np.nan,318,412]
    
})
stock_set2 = pd.DataFrame({
    "Date": ["2025-01-01", "2025-01-02", "2025-01-03"],
    'Tata Motors':[502,575,555],
    'Adani Energy':[302,402,394]
})

stock_setall = pd.merge(stock_set1,stock_set2)
print(stock_setall)

# 2. Handle missing dates for GOOGL (forward fill, interpolate) 
np.fill
stock_setall=stock_setall.fillna()
print(stock_setall)
# 3. Calculate daily returns for each stock 
# 4. Merge with market events and analyze impact 
# 5. Create a correlation matrix between stocks