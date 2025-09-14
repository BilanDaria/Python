import pandas
# For loop
# numbers = [1, 2, 3]
# new_numbers = []
# for i in numbers:
#     new_numbers.append(i+1)
# print(new_numbers)
from random import randint

# List Comprehension
# new_numbers_2 = [item + 1 for item in numbers]
# print(new_numbers_2)

# String as List
# name = "Daria"
# string_list = [i for i in name]
# print(string_list)

# Range as List
# range_as_list = [i * 2 for i in range(1, 5)]
# print(range_as_list)

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_name = [name for name in names if len(name) <= 4]
# print(short_name)
#
# long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)

# Dict Comprehension
# new_dict = {i: j for i, j in enumerate(names)}
# print(new_dict)

student_scores = {name: randint(1, 100) for name in names}
# print(student_scores)
#
# passed_students = {name: score for name, score in student_scores.items() if score >= 60}
# print(passed_students)

student_data_frame = pandas.DataFrame(student_scores.items(), columns=["Name", "Score"])
# print(student_data_frame)

for index, row in student_data_frame.iterrows():
    if row.Name == "Elanor":
        print(row.Score)
    
