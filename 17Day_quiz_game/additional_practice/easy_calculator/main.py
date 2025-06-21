from Calculator import Calculator

print("Possible math operation:\n"
      "add: +,\n"
      "subtract: -,\n"
      "multiply: *,\n"
      "divide: /")

expression = input("Enter expression (e.g., 5 * 2): ")

num1_str, operator, num2_str = expression.split()
num1 = float(num1_str)
num2 = float(num2_str)
calc = Calculator(num1, num2)

operations = {
    "+": calc.add(),
    "-": calc.subtract(),
    "*": calc.multiply(),
    "/": calc.divide(),
}

if operator in operations:
    result = operations[operator]
    print(f"{num1} {operator} {num2} = {result}")
else:
    print("Unsupported math operation!")

