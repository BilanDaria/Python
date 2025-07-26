from random import Random
from turtle import Turtle, Screen

random = Random()

tim = Turtle()
tim.shape("turtle")
tim.color("DarkOrchid4")
tim.speed(50)

screen = Screen()

# Draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

# Drawing different shape
# tim.teleport(0, 100, fill_gap=False)
# tim.width(3)
#
# for i in range(3, 11):
#     screen.colormode(255)
#     tim.pencolor(random.randint(0, 256), random.randint(0, 256),random.randint(0, 256))
#     degrees = 360 / i
#     for _ in range(i):
#         tim.left(-degrees)
#         tim.forward(60)

# Draw a random walk
# direction = {
#     1: tim.forward,
#     2: tim.back,
#     3: tim.right,
#     4: tim.left,
# }
# distance = 30
#
# tim.teleport(0, 100, fill_gap=False)
# tim.pensize(10)
# tim.speed(20)
#
# for _ in range(200):
#     screen.colormode(255)
#     tim.pencolor(random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
#     num = random.randint(1, 4)
#     if num == 3 or num == 4:
#         direction[num](90)
#         direction[random.randint(1, 2)](distance)

# Make a spirograph
n = 100
degree = 360 / n
for i in range(1, n+1):
    screen.colormode(255)
    tim.pencolor(random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
    tim.circle(radius=100)
    tim.left(degree)

screen.exitonclick()
