import pandas as pd

# 5. Combine different selection methods
orders = {
    'customer_name': ['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack',
                      'Alice', 'Leo', 'Mona', 'Nick', 'Olivia', 'Bob', 'Quinn', 'Rachel', 'Steve', 'Tina'],
    'category': ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Sports', 'Electronics', 'Clothing',
                 'Furniture', 'Groceries', 'Sports', 'Clothing', 'Furniture', 'Groceries', 'Electronics',
                 'Sports', 'Electronics', 'Clothing', 'Furniture', 'Groceries', 'Sports'],
    'order_value': [250, 150, 300, 180, 90, 220, 170, 310, 130, 260, 280, 190, 340, 110, 200, 270, 160, 230, 290, 140],
    'discount': [10, 20, 5, 18, 25, 12, 22, 16, 8, 15, 30, 14, 7, 19, 11, 21, 23, 9, 13, 17],
    'order_date': ['2026-06-15', '2026-06-10', '2026-05-20', '2026-06-18', '2026-04-25',
                   '2026-06-05', '2026-05-28', '2026-06-22', '2026-06-01', '2026-05-15',
                   '2026-06-12', '2026-05-30', '2026-06-08', '2026-04-10', '2026-06-25',
                   '2026-05-22', '2026-06-19', '2026-05-05', '2026-06-14', '2026-06-20']
}
orders = pd.DataFrame(orders)
orders['order_date'] = pd.to_datetime(orders['order_date'])
print(orders)

# 1. Find high-value orders (>$200) in Electronics category
a = orders[(orders['order_value'] > 200) & (orders['category'] == 'Electronics')]
print(a)

# 2. Select orders from last 30 days with discount > 15%
a = orders[(orders['order_date'] >= '2026-05-30') & (orders['discount'] > 15)]
print(a)

# 3. Create a subset with only customer_name, order_value, and calculated profit
orders['profit'] = orders['order_value'] - (orders['order_value'] * orders['discount'] / 100)
a = orders[['customer_name', 'order_value', 'profit']]
print(a)

# 4. Find customers who ordered both Electronics and Clothing
a = orders[orders['category'] == 'Electronics']['customer_name']
b = orders[orders['category'] == 'Clothing']['customer_name']
c = set(a).intersection(set(b))
d = orders[orders['customer_name'].isin(c)]
print(d)
