from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle

import time

STARTING_POSITIONS_FIRST_PADDLE = [(-370, 20), (-370, 0), (-370, -20)]
STARTING_POSITIONS_SECOND_PADDLE = [(370, 20), (370, 0), (370, -20)]

LINE_START_POSITION = (0, -350)
LEFT_SCORE_POSITION = (-150, 270)
RIGHT_SCORE_POSITION = (150, 270)

screen = Screen()
screen.setup(800, 700)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

line = Scoreboard(LINE_START_POSITION)
line.line()

paddle_1 = Paddle(STARTING_POSITIONS_FIRST_PADDLE)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    paddle_1.move_up()


screen.exitonclick()
