import data


def print_report():
    for i in data.resources:
        if i == 'water' or i == 'milk':
            print(f"{i.capitalize()}: {data.resources.get(i, 0)}ml.")
        else:
            print(f"{i.capitalize()}: {data.resources.get(i, 0)}g.")
    print(f"Money: ${data.money}")


def change_resource_amount(coffe_type):
    ingredients = list(data.resources.keys())
    for i in ingredients:
        data.resources[i] = data.resources.get(i) - data.MENU[coffe_type]["ingredients"][i]
    # print_report()


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
                return is_enough
        else:
            # print("Unnecessary ")
            continue
    return is_enough
    # print(needed_resources)


def coin_process():
    user_coins_amount = {
        "quarters": 0.00,
        "dimes": 0.00,
        "nickles": 0.00,
        "pennies": 0.00,
    }
    result = 0
    print("Please insert coins.")
    for j in user_coins_amount:
        user_coins_amount[j] = float(input(f"How many {j}?: "))
        print()
    # for i in data.COINS_COSTS:
    #     user_coins_amount[j] =





# while True:
#     user_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
#     if user_coffee == 'report':
#         print_report()
#     elif user_coffee == 'off':
#         print("Coffee machine turned off.")
#         break
#     elif user_coffee in data.MENU:
#         enough_resources = check_resources(user_coffee)
#         if not enough_resources:
#             break
#         price = data.MENU[user_coffee]["cost"]
#         # change =
#         # print(price)
#     else:
#         print("Sorry we don't produce this type of drinks. Please, choose from available menu 😉")



# Test prints
# check_resources("espresso")
# print_report()
# print("-----------------")
# print(data.MENU["latte"])
# print("-----------------")
# change_resource_amount("latte")
# print(data.COINS_COSTS.get("PENNY"))
coin_process()