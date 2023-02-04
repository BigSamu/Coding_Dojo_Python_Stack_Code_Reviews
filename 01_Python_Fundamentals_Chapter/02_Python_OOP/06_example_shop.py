class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self, name, products = []):
        self.name = name
        self.products = products
    def add_product(self, item):
        self.products.append(item)

jumbo = Shop("jumbo")
apple = Product("apple", 100)
milk = Product("milk", 120)
jumbo.add_product(apple)
jumbo.add_product(milk)

initial_products = [apple, milk]
lider = Shop("lider", initial_products)


for product in jumbo.products:
    print(f"{product.name} - {product.price}")

for product in lider.products:
    print(f"{product.name} - {product.price}")