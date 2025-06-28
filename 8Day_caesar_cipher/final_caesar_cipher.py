from logo import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_length = len(alphabet) - 1
isRestart = True

#TODO-1: Import and print the logo from art.py when the program starts.
print(art)
print("Hi! Let's start our program :)")

#TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

def ceasar(start_text, shift_amount, type):
    temp = ""
    new_index = 0
    for i in start_text:
        if not i.isalpha():
            temp += i
            continue
        index = alphabet.index(i)
        if type == "encode":
            new_index = index + shift_amount
            if new_index >= list_length:
                new_index = new_index - list_length - 1
        elif type == "decode":
            new_index = index - shift_amount
            if new_index < 0:
                new_index = new_index % list_length + 1
        else:
            print("Something goes wrong! Please, restart the program and try again.")
        temp += alphabet[new_index]
        # print(
        #     f'Letter: {i},  Index list: {index},  New index: {new_index}, New letter: {alphabet[new_index]}, Result: {temp}')
    print(f"Here's the {direction}d result: {temp}")



#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).
while(isRestart):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > list_length:
        shift = shift % list_length
    ceasar(text, shift, direction)
    answer = input("Do you want to restart the program? Type 'yes' for restart, type 'no' to stop:\n")
    print(answer)
    if answer == "no":
        isRestart = False
        print("Goodbye")

