#Creating a simple class with multiple objects

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

laptop1 = Laptop("Dell", 800)
laptop2 = Laptop("HP", 1000)

print(laptop1.brand, laptop1.price)
print(laptop2.brand, laptop2.price)
