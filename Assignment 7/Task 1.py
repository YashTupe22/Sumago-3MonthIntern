import pandas as pd
import numpy as np
# Objective: Master different types of joins
# 1.Create a comprehensive customer report showing: 
# Customer info, total orders, total spent
customer_info = pd.DataFrame({
    'ID':[101,102,103,104],
    'Name':['Yash','Atharv','Sanskar','Saheel']
})
Total_orders = pd.DataFrame({
    'ID':[101,102,105,104],
    'Product':['Laptop','Mobile','AC',"Tablet"],
    'Price':[75000,40000,43000,15000],
    'Orders':[3,5,2,7]
})
Total_spent = pd.DataFrame({
    'ID':[101,102,105,104],
    'Spent':[500000,70050,530042,100000]
})
report = pd.merge(customer_info,Total_orders,on="ID")
report = pd.merge(report,Total_spent,on="ID")
print(report)
#2. Analyze which customers haven't made any orders 
no_order = pd.merge(customer_info,Total_orders,on="ID",how="left")
no_order = no_order[no_order["Product"].isna()]
print(no_order)
#3. Create a product performance report 
Total_orders["Revenue"] = Total_orders['Price']*Total_orders['Orders']
per_report = Total_orders.groupby('Product')['Revenue'].sum()
print(per_report)
#4. Find orders with missing customer information 
no_order = pd.merge(Total_orders,customer_info,on="ID",how="left")
print(no_order)
#5. Create a complete order details view with customer and product info
c_o_detail = pd.merge(Total_orders,customer_info,on="ID",how="right")
Order = pd.merge(c_o_detail,Total_spent,on="ID",how="left")
print(Order)

