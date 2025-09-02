import pandas

# TODO 1. Read data from cvs file
# TODO 2. Count how many squirrels of each color in this table (gray, cinnamon, black)
# TODO 3. Create a new table with data: num_of_squirrels, fur_color

squirrel_table = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# print(squirrel_table)

# squirrel_table_color_list = squirrel_table["Primary Fur Color"].to_list()
# print(squirrel_table_color_list)

black_squirrels = (squirrel_table["Primary Fur Color"] == "Black").sum()
print(f"{black_squirrels = }")
gray_squirrels = (squirrel_table["Primary Fur Color"] == "Gray").sum()
print(f"{gray_squirrels = }")
cinnamon_squirrels = (squirrel_table["Primary Fur Color"] == "Cinnamon").sum()
print(f"{cinnamon_squirrels = }")

fur_color_set = set([i for i in squirrel_table["Primary Fur Color"] if str(i) != "nan"])
print(fur_color_set)

squirrel_dict = {
    "Fur color": ["Black", "Gray", "Cinnamon"],
    "Amount": [black_squirrels, gray_squirrels, cinnamon_squirrels]
}
data = pandas.DataFrame(squirrel_dict)
print(data)
data.to_csv("fur_squirrel_count.csv")
