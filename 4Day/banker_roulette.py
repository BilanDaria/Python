import random

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
print(names)

lucky_guy_number = random.randint(0, len(names)-1)
lucky_guy_name = names[lucky_guy_number]

print(f"{lucky_guy_name} is going to buy the meal today!")
