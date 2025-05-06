alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
list_length = len(alphabet) - 1

def encrypt(plain_text, shift_amount):
    temp = ""
    for i in plain_text:
        index = alphabet.index(i)
        new_index = index + shift_amount
        if new_index >= list_length:
            new_index = new_index - list_length
        temp += alphabet[new_index]
        print(
            f'Letter: {i},  Index list: {index},  New index: {new_index}, New letter: {alphabet[new_index]}, Encripting: {temp}')

# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  # e.g.
  # cipher_text = "mjqqt"
  # shift = 5
  # plain_text = "hello"
  # print output: "The decoded text is hello"


def decrypt(encrypt_text, shift_amount):
    temp = ""
    for i in encrypt_text:
        index = alphabet.index(i)
        new_index = index - shift_amount
        if new_index < 0:
            new_index = new_index % list_length
        temp += alphabet[new_index]
        print(
            f'Letter: {i},  Index list: {index},  New index: {new_index}, New letter: {alphabet[new_index]}, Encripting: {temp}')



# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Something goes wrong! Please, restart the program and try again \-_-/")



# try to do checking did user encrypt any word before
# encrypt_word = ""
# encrypt_word = encrypt(text, shift)
# decrypt(encrypt_word, shift)