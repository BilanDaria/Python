from replit import clear
from art import logo
# Calculator
# Add


def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


math_operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
is_calculating = True
first_answer = 0
second_answer = 0


def calculator():
    print(logo)

    num1 = float(input("What's the first number? : "))
    for i in math_operations:
        print(i)

    while is_calculating:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? : "))

        if operation in math_operations:
            calculation = math_operations[operation]
            answer = calculation(num1, num2)
        else:
            print("Invalid math operation!")
            break
        print(f"{num1} {operation} {num2} = {answer}")

        is_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation.: ")
        if is_continue == "n":
            clear()
            calculator()
        elif is_continue == "y":
            num1 = answer
            continue
            # operation = input("Pick an operation: ")
            # num3 = float(input("What's the next number? : "))
            #
            # if operation in math_operations:
            #     calculation = math_operations[operation]
            #     second_answer = calculation(first_answer, num3)
        else:
            print("Invalid math operation!")
            break


calculator()

