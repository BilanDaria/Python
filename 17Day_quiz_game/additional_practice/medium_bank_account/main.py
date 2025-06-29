from bank_system import BankSystem

bank = BankSystem()

menu = {
    1: bank.create_account,
    2: bank.find_account,
    3: bank.deposit_to_account,
    4: bank.withdraw_from_account,
    5: bank.__str__,
    6: None,
}


def get_amount(prompt="Enter amount: "):
    try:
        return float(input(prompt))
    except ValueError:
        print("Entered value should be a number.")
        return get_amount()


def get_owner(prompt="Enter your account number: "):
    return input(prompt)


def main_block():
    while True:
        try:
            option = int(input("Menu:\n"
                               "1. Create new bank account,\n"
                               "2. Check your balance.\n"
                               "3. Make deposit.\n"
                               "4. Withdraw money.\n"
                               "5. Get all accounts.\n"
                               "6. Tun off system.\n"))
        except ValueError:
            print("Invalid option type.")
            continue
        if option not in menu:
            print("Unsupported option.")
            continue
        if option == 6:
            print("System shuts down complete.")
            break
        elif option == 1:
            print(menu[option](get_amount()))
        elif option == 2:
            account = menu[option](get_owner())
            print(account if account else "Account not found")
        elif option in (3, 4):
            menu[option](get_owner(), get_amount())
        else:
            print(bank)


print("Welcome to Bank System!")
main_block()
