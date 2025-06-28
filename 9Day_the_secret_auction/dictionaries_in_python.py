python_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving data from dictionary
# print(python_dictionary["Bug"])

# Adding new items to dictionary
python_dictionary["Loop"] = "The action of doing something over and over again."
# print(python_dictionary)

# Create an empty dictionary
empty_dict = {}

# Wipe an existing dictionary
# python_dictionary = {}
# print(python_dictionary)

# Edit an item in a dictionary
# print(python_dictionary["Bug"])
python_dictionary["Bug"] = "A moth in your computer"
# print(python_dictionary["Bug"])

# Loop throught a dictionary
for key in python_dictionary:
    print(key)
    print(python_dictionary[key])

