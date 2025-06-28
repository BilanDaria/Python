from Product import Product
from Inventory import Inventory
from data import product_data

# Initiate global variable
money = 0

# Initiate basic product data
products = []
for i in product_data:
    new_product = Product(**i)
    products.append(new_product)

# Initiate inventory object
manager = Inventory(products)

# Menu options
menu = {
    1: manager.list_product,
    2: manager.add_product,
    3: manager.find_product,
    4: manager.sell_product,
    5: manager.restock_product,
}


def get_product_info():
    print("For adding new product you should input name, quantity and price per unit.")
    name = input("Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per unit: "))
    return name, quantity, price


def get_product_name():
    return input("Enter product name: ")


def get_amount(prompt="Enter amount: "):
    return int(input(prompt))


def main_logic():
    global money
    while True:
        try:
            option = int(input("Please, choose what you want to do:\n"
                               "1 - get all products,\n"
                               "2 - add new product,\n"
                               "3 - find the product,\n"
                               "4 - buy the product,\n"
                               "5 - restock the product,\n"
                               "6 - our current zoloto,\n"
                               "0 - turn off the system.\n"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 0:
            print("System shuts down complete.")
            break
        elif option == 6:
            print(f"Zoloto: {money}")
            continue
        if option not in menu:
            print("Unsupported menu option. Try again!")
            continue

        if option == 1:
            print(menu[option]())
        elif option == 2:
            name, quantity, price = get_product_info()
            menu[option](name, quantity, price)
            print(f"{name} was successfully added to the our list of products.\n{menu[3](name)}")
        elif option == 3:
            product = menu[option](get_product_name())
            if not product:
                print("Product was not found.")
                continue
            print(product)
        elif option == 4:
            money += menu[option](get_product_name(), get_amount(), money)
        else:
            menu[option](get_product_name(), get_amount())



main_logic()
