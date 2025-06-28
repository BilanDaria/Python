# Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

is_game_end = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ["_" for i in range(len(chosen_word))]

print(stages[6])

# End up suggested code
while not is_game_end:
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    guess = input("Write a letter:\n").lower()

    # Check guessed letter

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        print(f"Lives left: {lives}")
        if lives == 0:
            print('You lose!')
            is_game_end = True

    # Check if user has got all letters.
    if '_' not in display:
        print('You win!')
        is_game_end = True

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    if lives < 6:
        print(stages[lives])


# Full my solution
# while not is_game_end:
#     # Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")
#     guess = input("Write a letter:\n").lower()
#
#     # Check guessed letter
#     if guess.isalpha():
#         if len(guess) == 1:
#             if guess in chosen_word:
#                 for i in range(len(chosen_word)):
#                     if chosen_word[i] == guess:
#                         display[i] = guess
#             else:
#                 lives -= 1
#                 print(f"Lives left: {lives}")
#                 if lives == 0:
#                     print('You lose!')
#                     is_game_end = True
#         else:
#             print("Error input length! You can type only 1 letter!")
#     else:
#         print("Error input type! Try again and input a letter!")
#
#     # Check if user has got all letters.
#     if '_' not in display:
#         print('You win!')
#         is_game_end = True
#
#     if lives < 6:
#         print(stages[lives])
