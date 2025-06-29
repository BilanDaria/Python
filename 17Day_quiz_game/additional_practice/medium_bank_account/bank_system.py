from bank_account import BankAccount
from random import Random

random = Random()


class BankSystem:
    last_account_number = 0

    def __init__(self):
        self.accounts = []

    def create_account(self, balance):
        owner = f"{self.last_account_number + 1:03d}"
        self.last_account_number = int(owner)

        new_account = BankAccount(owner, balance)
        self.accounts.append(new_account)
        return (f"Account successfully added.\n"
                f"{new_account}")

    def find_account(self, owner):
        account = next((i for i in self.accounts if owner == i.owner), None)
        return account

    def deposit_to_account(self, owner, amount):
        account = self.find_account(owner)
        if not account:
            print("Account not found.")
            return
        account.deposit(amount)

    def withdraw_from_account(self, owner, amount):
        account = self.find_account(owner)
        if not account:
            print("Account not found.")
            return
        account.withdraw(amount)

    def __str__(self):
        return '\n'.join(str(i) for i in self.accounts)
