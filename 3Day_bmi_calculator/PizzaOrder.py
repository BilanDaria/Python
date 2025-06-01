print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25

if size.upper() == "S":
    bill += small_pizza
elif size.upper() == "M":
    bill += medium_pizza
else:
    bill += large_pizza

if add_pepperoni.upper() == "Y":
    if size.upper() == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese.upper() == "Y":
    bill += 1

print("Thank you for choosing Python Pizza Deliveries! "
      f"Your final bill is: $ {bill}.")

