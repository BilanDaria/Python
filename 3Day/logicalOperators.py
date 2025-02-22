height = int(input("What is your height in cm? "))
bill =0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("Child tickets are 5$.")
        bill = 5
    elif 12 <= age < 18:
        print("Youth tickets are 7$.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Sale prize! 0$ for ticket.")
    else:
        print("Adults ticket are 12$.")
        bill = 12

    is_taking_photo = input("Do you want to take a photo? Y or N. ")
    if is_taking_photo.upper() == "Y":
        print(f"The total bill {bill + 3}")

else:
    print("Sorry, you have to grow taller before you can ride.")
