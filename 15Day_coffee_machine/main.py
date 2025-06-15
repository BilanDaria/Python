import data


def print_report():
    for i in data.resources:
        if i == 'water' or i == 'milk':
            print(f"{i.capitalize()}: {data.resources.get(i, 0)}ml.")
        else:
            print(f"{i.capitalize()}: {data.resources.get(i, 0)}g.")
    print(f"Money: ${round(data.money, 2)}")


def print_menu():
    print("MENU ☕:")
    for i in data.MENU:
        print(f"{i.upper()} - ${data.MENU[i]['cost']}")


def print_result(users_change, coffe_type):

    if users_change < 0:
        print(f"Here is {users_change * -1} in change.\n"
              f"Here your {coffe_type}. ☕")
        change_resource_amount(coffe_type)
    elif users_change == 0:
        print(f"Here your {coffe_type}. ☕")
        change_resource_amount(coffe_type)
    else:
        print("Sorry there is not enough money. Money refunded.")


def change_resource_amount(coffee_type):
    ingredients = list(data.resources.keys())
    for i in ingredients:
        if i in data.MENU[coffee_type]["ingredients"]:
            data.resources[i] = data.resources.get(i) - data.MENU[coffee_type]["ingredients"][i]
        else:
            continue
    # print_report()    # Test print


def check_resources(coffee_type):
    needed_resources = list(data.resources.keys())
    is_enough = False
    for i in needed_resources:
        if i in data.MENU[coffee_type]["ingredients"]:
            if data.resources.get(i) > data.MENU[coffee_type]["ingredients"][i]:
                is_enough = True
            else:
                is_enough = False
                print(f"Sorry there is not enough {i}.")
        else:
            continue
    return is_enough
    # print(needed_resources)   # Test print


def coin_process(coffee_cost):
    user_coins_amount = {
        "quarters": 0.00,
        "dimes": 0.00,
        "nickles": 0.00,
        "pennies": 0.00,
    }
    result = 0.0
    print("Please insert coins.")
    for i, j in zip(user_coins_amount, data.COINS_COSTS):
        user_coins_amount[i] = float(input(f"How many {i}?: ")) * data.COINS_COSTS[j]
    user_input = round(sum(list(user_coins_amount.values())))
    print(f"Your money: {user_input}")
    result += round((coffee_cost - user_input), 2)
    if result < 0 or result == 0:
        data.money += sum(list(user_coins_amount.values())) + result
    return result


def main():
    while True:
        user_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_coffee == 'report':
            print_report()
        elif user_coffee == 'menu':
            print_menu()
        elif user_coffee == 'off':
            print("Coffee machine turned off.")
            break
        elif user_coffee in data.MENU:
            enough_resources = check_resources(user_coffee)
            if not enough_resources:
                break
            price = data.MENU[user_coffee]["cost"]
            # print(f"Price is: {price}")         # Test print
            change = coin_process(price)
            # print(f"Change will be: {change}")  # Test print
            print_result(change, user_coffee)
        else:
            print("Sorry we don't produce this type of drinks. Please, choose from available menu 😉")


print_menu()
main()

# Test prints
# check_resources("espresso")
# print_report()
# print("-----------------")
# print(data.MENU["latte"])
# print("-----------------")
# change_resource_amount("latte")
# print(data.COINS_COSTS.get("PENNY"))
# coin_process()