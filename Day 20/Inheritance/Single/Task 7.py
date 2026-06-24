class product:
    def fetch(self):
        self.product_name = input("Enter Produt Name")
        self.price = int(input("Enter product Price"))

class Electronics(product):
    def details(self,warranty_years):
        self.warranty = warranty_years
        print(f"\tProduct Details\n1.Product Name: {self.product_name}\n2.Product Price: {self.price}\n3.Warranty: {warranty_years} years")

e = Electronics()