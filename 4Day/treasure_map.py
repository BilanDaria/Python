import re
from pprint import pprint

row_count = 3

line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]
map = [line1, line2, line3]


print("Hiding your treasure! X marks the spot.")
position = input().capitalize()

# 1 way
# START
# coordinates = re.split('(\d+)', position)
# coordinates = [i for i in coordinates if i]
# print(coordinates)
#
# for i in map:
#     pprint(i)
# print()
#
# if coordinates[0] == "A" and int(coordinates[1]) < row_count:
#     map[int(coordinates[1])-1][0]= "❌ "
# elif coordinates[0] == "B" and int(coordinates[1]) < row_count:
#     map[int(coordinates[1])-1][1] = "❌ "
# elif coordinates[0] == "C" and int(coordinates[1]) < row_count:
#     map[int(coordinates[1])-1][2] = "❌ "
# else:
#     print("Here is an error! The field has only 3 columns that are indexed with A, B, or C! "
#           "And 3 rows that are indexed like 1, 2, 3.\n"
#           "Please, rerun the program and try one more time )")
#     exit()
# END

# 2 way
# START
alfa_part = position[0]
numeric_part = int(position[1]) - 1

print(f"Alfa: {alfa_part}\t Numeric: {numeric_part}")

if alfa_part == "A" and numeric_part < row_count:
    map[numeric_part][0] = "❌ "
elif alfa_part == "B" and numeric_part < row_count:
    map[numeric_part][1] = "❌ "
elif alfa_part == "C" and numeric_part < row_count:
    map[numeric_part][2] = "❌ "
else:
    print("Here is an error! The field has only 3 columns that are indexed with A, B, or C!\n"
          "Please, rerun the program and try ine more time )")
    exit()
# END

for i in map:
    pprint(i)
