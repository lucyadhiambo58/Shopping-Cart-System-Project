#write a program that simulates a simple shopping cart system. The program should have a class product that represents a product and provides methods for getting and setting the product's name, price and quantity. The program should also have a class cart that represents a shopping cart and provide methods for adding products to the cart, removing products from the cart and calculating the total cost of the products in the cart.

#Define the product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for p in self.products:
            if p.get_name() == product_name:
                self.products.remove(p)
                break

    def total_cost(self):
        total_cost = sum(product.get_price() * product.get_quantity() for product in self.products)
        return total_cost


    

