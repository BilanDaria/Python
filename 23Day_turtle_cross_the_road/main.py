from time import sleep
from turtle import Screen
from turtle_tommy import Tommy
from blocks import Block

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

block = Block()

tommy = Tommy()

screen.listen()
screen.onkeypress(tommy.move_up, "w")
screen.onkeypress(tommy.move_down, "s")
screen.onkeypress(tommy.move_right, "d")
screen.onkeypress(tommy.move_left, "a")

is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.1)




screen.exitonclick()
