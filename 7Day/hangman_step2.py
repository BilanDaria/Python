# Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# index = 0

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = ["_" for i in range(len(chosen_word))]

# Testing code
print(display)

guess = input("Write a letter:\n").lower()
print("Guessing in progress...")

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# Solution using index variable with value len(chosen_word)
# if guess.isalpha():
#     for i in chosen_word:
#         if i == guess:
#             print("Right")
#             display[index] = guess
#         else:
#             print("Wrong")
#         print(f"index: {index}")
#         index += 1
# else:
#     print("Error input type! Try again and input a letter!")

if guess.isalpha():
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
else:
    print("Error input type! Try again and input a letter!")

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
