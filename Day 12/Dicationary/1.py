d = {"id":1,
     "name":'Yash',
     'desg':'da',
     'salary':75000}

print(d)
print(d.keys())
print(d.items())
print(d.popitem())
d.update({"Salary":100000})
print(d)
print(d.get("Salary"))