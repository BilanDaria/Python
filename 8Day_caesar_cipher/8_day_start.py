# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# Simple function
# def greet():
#     print('Good morning!')
#     print('Good day!')
#     print('Good evening!')
#
#
# greet()

# Function that allows for input
# def greet_with_name(name):
#     print(f'Good morning, {name}!')
#     print(f'Good day, {name}!')
#     print(f'Good evening, {name}!')
#
#
# greet_with_name('Daria')


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}")


greet_with("Daria", "Kyiv")
# keyword arguments
greet_with(location="Kyiv", name="Daria")
