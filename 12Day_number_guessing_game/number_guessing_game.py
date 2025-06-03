# TODO 1. create 2 constants for easy = 10 and hard = 5 levels

# TODO 2. generate a guessed number

# TODO 3. Write a starting block. Ask about prefer level

# TODO 4. Create main logic to check user number and compare it with guessed one

import random

from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

is_game_active = True
secret_number = random.randint(1, 100)


def guessing_number(attempts):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        number = int(input("Make a guess: "))

        if number == secret_number:
            print(f"You got it! The answer was {secret_number}.")
            return False
        elif number < secret_number:
            print("Too low.\n"
                  "Guess again.")
            attempts -= 1
        elif number > secret_number:
            print("Too high.\n"
                  "Guess again.")
            attempts -= 1
        else:
            print("Something goes wront")
            break
    else:
        print("You've run out of guesses. Restart the program to run again.")


print(logo)
print("Welcome to the Number Guessing Game!")


while is_game_active:
    attempts = 0
    print("I'm thinking of number between 1 and 100.")
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_level == 'easy':
        is_game_active = guessing_number(EASY_LEVEL)
        continue
    elif game_level == "hard":
        is_game_active = guessing_number(HARD_LEVEL)
        continue
    else:
        print("Invalid hard level. Try again.")


