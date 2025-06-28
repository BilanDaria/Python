# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkBlue")
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# # Draw a square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
# my_screen.exitonclick()

from prettytable import PrettyTable, TableStyle
from prettytable.colortable import ColorTable, Themes

table = PrettyTable()
table_style = TableStyle(16)
table.set_style(table_style)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)

color_table = ColorTable(theme=Themes.DYSLEXIA_FRIENDLY)
color_table.align = 'r'
color_table.field_names = ["Pokemon Name", "Type"]
color_table.add_row(["Pikachu", "Electric"])
color_table.add_divider()
color_table.add_row(["Squirtle", "Water"])
color_table.add_divider()
color_table.add_row(["Charmander", "Fire"])
print(color_table)

