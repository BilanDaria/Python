
# For loop
numbers = [1, 2, 3]
new_numbers = []
for i in numbers:
    new_numbers.append(i+1)
print(new_numbers)

# List Comprehension
new_numbers_2 = [item + 1 for item in numbers]
print(new_numbers_2)

# String as List
name = "Daria"
string_list = [i for i in name]
print(string_list)

# Range as List
range_as_list = [i * 2 for i in range(1, 5)]
print(range_as_list)

# Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_name = [name for name in names if len(name) <= 4]
print(short_name)

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)
