print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("How old are you? "))
#     if age < 12:
#         print("You should pay 5$ for ticket.")
#     elif 12 < age < 18:
#         print("You should pay 7$ for ticket.")
#     else:
#         print("You should pay 12$ for ticket.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


height = int(input("What is your height in cm? "))
bill =0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("Child tickets are 5$.")
        bill = 5
    elif 12 < age < 18:
        print("Youth tickets are 7$.")
        bill = 7
    else:
        print("Adults ticket are 12$.")
        bill = 12

    is_taking_photo = input("Do you want to take a photo? Y or N. ")
    if is_taking_photo.upper() == "Y":
        print(f"The total bill {bill + 3}")

else:
    print("Sorry, you have to grow taller before you can ride.")
