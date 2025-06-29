class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print(f"You can't deposit ${amount}.\n"
                  f"Transaction canceled.\n")
        else:
            self.balance += amount
            print(f"Payment success.\n"
                  f"Your current balance: {self.balance}\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.\n"
                  "Transaction canceled.\n")
        elif amount > self.balance:
            print(f"You can't withdraw ${amount}.\n"
                  f"Current balance: {self.balance}.\n"
                  f"Transaction canceled.\n")
        else:
            self.balance -= amount
            print("Withdraw success.\n"
                  f"Current balance: {self.balance}\n")

    def __str__(self):
        return (f'Owner: {self.owner},\n'
                f'Balance: {self.balance}\n')
