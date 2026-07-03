import pandas as pd
data = pd.DataFrame({
    'Date' : pd.date_range("2026-01-01",periods=12,freq="n"),
    'Region' : ["North",'South','East','West']*3,
    'Product':['A','B']*6,
    'Sales' : [100,150,200,120,100,160,140,190,110,170,130,200],
    'Profit':[20,30,40,24,36,32,28,38,22,24,34,26]
})
# Group by single Column
region_sales = data.groupby('Region')['Sales'].sum()
print(region_sales)

#Group by Multiple Column
region_product_sales = data.groupby(['Region','Product'])['Sales'].sum()
print(region_product_sales)

# Multiple Aggeration
region_stats = data.groupby('Region').agg({
    'Sales': ['sum','mean','count']
})
print(region_stats)

def top_sales(group):
    return group.nlargest(2,'Sales')

top_by_region = data.groupby('Region').apply(top_sales)
print(top_by_region)

data['Sales_mean_by_region'] = data.groupby('Region')['Sales'].transform('mean')
data['Sales_normalized'] = data.groupby('Region')['Sales'].transform(lambda x: x/x.sum())
print(data)

# Group by using filter/condition
large_region=data.groupby('Region').filter(lambda x: x["Sales"].sum()>500)
print(large_region)

for name,group in data.groupby('Region'):
    print(f"Region: {name}")
    print(group)

result = data.groupby("Region").agg