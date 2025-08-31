#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open('Input/Names/invited_names.txt') as file:
    names = file.readlines()
with open("Input/Letters/starting_letter.txt") as file:
    letter_text = file.read()


for i in names:
    strip_name = i.strip('\n')
    new_letter = letter_text.replace(PLACEHOLDER, strip_name)
    with open(f'Output/ReadyToSend/letter_for_{strip_name}', mode='w') as file:
        file.write(new_letter)
