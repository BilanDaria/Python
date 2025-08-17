import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from random import choice

RIGHT_X_POS = 350
LEFT_X_POS = -350
Y_POS = 0

BALL_DIRECTION = [1, -1]

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

scoreboard = Scoreboard()
right_paddle = Paddle((RIGHT_X_POS, Y_POS))
left_paddle = Paddle((LEFT_X_POS, Y_POS))
ball = Ball()
ball.x_move_step *= choice(BALL_DIRECTION)
ball.y_move_step *= choice(BALL_DIRECTION)

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with a right paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 335 or ball.distance(
            left_paddle) < 35 and ball.xcor() > -345:
        ball.increase_ball_speed()
        ball.bounce_x()

    # Detect missing right paddle
    if ball.xcor() > 385:
        ball.reset_position()
        scoreboard.l_point()

    # Detect missing left paddle
    if ball.xcor() < -385:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
