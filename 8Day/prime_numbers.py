# Write your code below this line 👇
import math


def prime_checker(number):
    is_prime = True
    if number < 2:
        is_prime = False
    elif number == 2 or number == 3:
        is_prime = True
    elif number % 2 == 0:
        is_prime = False
    else:
        max_range = math.isqrt(number) + 1
        for i in range(3, max_range, 2):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
