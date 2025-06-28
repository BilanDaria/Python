from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

###### All imported packeges was getting from course materials as starting conditions ######


def main():
    while True:
        user_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_coffee == 'report':
            coffee.report()
            money.report()
        elif user_coffee == 'menu':
            print(menu.get_items())
        elif user_coffee == 'off':
            print("Coffee machine turned off.")
            break
        else:
            user_drink = menu.find_drink(user_coffee)
            if coffee.is_resource_sufficient(user_drink):
                if money.make_payment(user_drink.cost):
                    coffee.make_coffee(user_drink)
                else:
                    continue
            else:
                break


main()

