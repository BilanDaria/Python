from Calculator import Calculator

print("Possible math operation:\n"
      "add: +,\n"
      "subtract: -,\n"
      "multiply: *,\n"
      "divide: /")
num1 = float(input("Number 1: "))
operation = input("Operation: ")
num2 = float(input("Number 2: "))
calc = Calculator(num1, num2)


if operation == "+":
    result = calc.add()
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = calc.subtract()
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = calc.multiply()
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    result = calc.divide()
    print(f"{num1} / {num2} = {result}")
else:
    print("Unsupported math operation!")

