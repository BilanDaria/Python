from turtle import Turtle, Screen
from random import Random

# polygon 10x10
# each dot radius = 20
# space between the dots 50

random = Random()
step = 50
width = 10
height = 10

colors_list = [(216, 220, 217), (186, 162, 142), (130, 86, 71), (51, 36, 28), (174, 178, 175), (226, 211, 114), (211, 221, 228), (21, 27, 50), (113, 168, 200), (176, 148, 60), (75, 106, 153), (77, 108, 91), (205, 84, 105), (223, 212, 218), (103, 41, 32), (186, 153, 165), (57, 36, 52), (146, 55, 67), (215, 98, 51), (25, 60, 135), (81, 119, 182), (98, 142, 134), (188, 194, 188), (219, 172, 181), (38, 82, 71), (85, 46, 76), (35, 50, 43), (221, 179, 169), (184, 190, 203), (69, 65, 55), (177, 196, 203), (96, 137, 156), (31, 72, 94)]

screen = Screen()
screen.screensize(2000, 1500)
screen.colormode(255)
dot = Turtle()
dot.hideturtle()
dot.speed(50)
dot.up()

print(dot.position())
dot.teleport(-225, -225)    # start position
# dot.dot(20, random.choice(colors_list))
# print(dot.position())
# dot.teleport(255, -255)     # last position for 1 line
# dot.dot(20, random.choice(colors_list))
# print(dot.position())
# dot.teleport(-255, 255)     # first position for last line
# dot.dot(20, random.choice(colors_list))
# print(dot.position())
# dot.teleport(255, 255)     # last position for last line
# dot.dot(20, random.choice(colors_list))
# print(dot.position())
# dot.teleport(0, -255)     # first position for last line
# dot.dot(20, random.choice(colors_list))


for _ in range(height):
    first_line_pos = dot.pos()
    for _ in range(width):
        print(dot.position())
        dot.dot(20, random.choice(colors_list))
        dot.forward(step)
    dot.teleport(first_line_pos[0], first_line_pos[1] + step)


screen.exitonclick()
