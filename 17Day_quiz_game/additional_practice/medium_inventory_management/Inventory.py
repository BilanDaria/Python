from Product import Product


class Inventory:
    def __init__(self, products):
        self.products = products

    def add_product(self, name, quantity, price):
        new_product = Product(name, quantity, price)
        self.products.append(new_product)

    def find_product(self, product_name):
        # result = list(filter(lambda p: p.name == product_name, self.products))
        # print('\n'.join(str(i) for i in result))
        result = next((i for i in self.products if product_name == i.name), None)
        return result

    def list_product(self):
        return '\n'.join((str(i) for i in self.products))

    def sell_product(self, name, amount, money):
        product = self.find_product(name)
        if product:
            money += product.sell(amount, money)
            return money
        else:
            print("Product not found.")
            return 0

    def restock_product(self, name, amount):
        product = self.find_product(name)
        if product:
            product.restock(amount)
            self.find_product(name)
        else:
            print("Product not found.")
            return 0
