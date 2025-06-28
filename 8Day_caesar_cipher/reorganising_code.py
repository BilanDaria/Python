alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
list_length = len(alphabet) - 1


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def ceasar(start_text, shift_amount, type):
    temp = ""
    new_index = 0
    for i in start_text:
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


# def encrypt(plain_text, shift_amount):
#     temp = ""
#     for i in plain_text:
#         index = alphabet.index(i)
#         new_index = index + shift_amount
#         if new_index >= list_length:
#             new_index = new_index - list_length
#         temp += alphabet[new_index]
#         print(
#             f'Letter: {i},  Index list: {index},  New index: {new_index}, New letter: {alphabet[new_index]}, Encripting: {temp}')
#
# def decrypt(encrypt_text, shift_amount):
#     temp = ""
#     for i in encrypt_text:
#         index = alphabet.index(i)
#         new_index = index - shift_amount
#         if new_index < 0:
#             new_index = new_index % list_length
#         temp += alphabet[new_index]
#         print(
#             f'Letter: {i},  Index list: {index},  New index: {new_index}, New letter: {alphabet[new_index]}, Encripting: {temp}')
#
#
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("Something goes wrong! Please, restart the program and try again \-_-/")

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
ceasar(text, shift, direction)
