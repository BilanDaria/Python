class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def sell(self, amount, money):
        if self.quantity == 0:
            print(f"Sorry, {self.name} is out of stock.")
            return 0
        if amount <= 0:
            print(f"You can't by {amount} of {self.name}.\nRequest canceled!")
            return 0
        elif amount > self.quantity:
            print(f"We don't have enough {self.name}. Current amount: {self.quantity}")
            ans = input(f"Would you like to get {self.quantity} {self.name}s?: ")
            if ans == 'yes':
                money += self.price * self.quantity
                self.quantity = 0
                print(f"Thanks for buying {self.name}.")
                self.__str__()
                return money
            elif ans == 'no':
                print("Request canceled!")
                return 0
            else:
                print("Unknown answer. Request canceled!")
                return 0
        else:
            money += self.price * amount
            self.quantity -= amount
            print(f"Thanks for buying {self.name}.")
            self.__str__()
            return money

    def restock(self, amount):
        self.quantity += amount
        self.__str__()

    def __str__(self):
        return (f"Product name: {self.name}\n"
                f"Quantity: {self.quantity}\n"
                f"price: {self.price}\n")
