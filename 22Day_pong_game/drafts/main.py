from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle

import time
LEFT_X_COORD = -370
RIGHT_X_COORD = 370

STARTING_POSITIONS_FIRST_PADDLE = [(LEFT_X_COORD, 20), (LEFT_X_COORD, 0), (LEFT_X_COORD, -20)]
STARTING_POSITIONS_SECOND_PADDLE = [(RIGHT_X_COORD, 20), (RIGHT_X_COORD, 0), (RIGHT_X_COORD, -20)]

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

paddle_1 = Paddle(STARTING_POSITIONS_FIRST_PADDLE, LEFT_X_COORD)

screen.listen()
screen.onkey(paddle_1.up, "W")
screen.onkey(paddle_1.down, "S")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    game_is_on = paddle_1.move()


screen.exitonclick()
