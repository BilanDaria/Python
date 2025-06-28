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

# function = math_operation['*']
# function(2, 3)

num1 = float(input("What's the first number? : "))
first_answer = 0
second_answer = 0
for i in math_operations:
    print(i)
operation = input("Pick an operation from the line above: ")
num2 = float(input("What's the second number? : "))

if operation in math_operations:
    calculation = math_operations[operation]
    first_answer = calculation(num1, num2)

print(f"{num1} {operation} {num2} = {first_answer}")

operation = input("Pick an operation from the line above: ")
num3 = float(input("What's the second number? : "))
if operation in math_operations:
    calculation = math_operations[operation]
    second_answer = calculation(calculation(num1, num2), num3)

print(f"{first_answer} {operation} {num3} = {second_answer}")
