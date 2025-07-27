from turtle import Screen
from scoreboard import Scoreboard

import time

STARTING_POSITIONS_FIRST_PADDLE = [(-285, 20), (-285, 0), (-285, -20)]
STARTING_POSITIONS_SECOND_PADDLE = [(285, 20), (285, 0), (285, -20)]

LINE_START_POSITION = (0, -300)
LEFT_SCORE_POSITION = (-150, 270)
RIGHT_SCORE_POSITION = (150, 270)

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

line = Scoreboard(LINE_START_POSITION)
left_score = Scoreboard(LEFT_SCORE_POSITION)
left_score.score_counter_update("left")



screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")


game_is_on = True
while game_is_on:
    line.line()
    break
    # screen.update()
    # time.sleep(0.1)


screen.exitonclick()
