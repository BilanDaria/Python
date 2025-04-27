#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ["_" for i in range(len(chosen_word))]

is_guessed = False

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.


while not is_guessed:
    print(display)
    guess = input("Write a letter:\n").lower()

    # Check guessed letter
    if guess.isalpha():
        if len(guess) == 1:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess
        else:
            print("Error input length! You can type only 1 letter!")
    else:
        print("Error input type! Try again and input a letter!")

    if '_' not in display:
        print('You win!')
        is_guessed = True

print(display)
