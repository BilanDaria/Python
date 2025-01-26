print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?\n$ "))
tip = int(input("How much tip would you like to give? % 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))

tip = (total_bill * tip) / 100
total_bill += tip
result = total_bill / people
# result = (total_bill + tip) / people
print(f"Each person should pay: {round(result, 2)}")
