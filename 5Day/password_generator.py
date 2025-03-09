# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_of_letters = int(input("How many letters would you like in you password?\n"))
num_of_symbols = int(input("How many symbols would you like?\n"))
num_of_numbers = int(input("How many numbers would you like?\n"))

password_length = num_of_numbers + num_of_symbols + num_of_letters
first_list = []
password = ""

for _ in range(num_of_letters):
    # letter_index = random.randint(0, len(letters) - 1)
    # first_list.append(letters[letter_index])
    first_list.append(random.choice(letters))

for _ in range(num_of_symbols):
    # symbol_index = random.randint(0, len(symbols) - 1)
    # first_list.append(symbols[symbol_index])
    first_list.append(random.choice(symbols))

for _ in range(num_of_numbers):
    # number_index = random.randint(0, len(numbers) - 1)
    # first_list.append(numbers[number_index])
    first_list.append(random.choice(numbers))

print(first_list)
random.shuffle(first_list)
print(first_list)

for i in first_list:
    password += i
print(f"Your passwords is: {password}")

