from turtle import Turtle
from random import choice, randint

last_y_position = -300

START_X_POSITION = 280
BLOCK_COLORS = ["Red", "LightPink", "Green", "Yellow", "Black", "DeepSkyBlue", "Orange", "Purple", "Pink", "Brown", "Gray", "Cyan",
                "Magenta"]


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(270)
        self.shapesize(2, 1)
        self.penup()
        self.color(choice(BLOCK_COLORS))
        # self.goto(280, self.get_to_new_position())
        # self.goto(randint(-280, 280), self.get_to_new_position())
        self.goto(self.get_start_x_position(), self.get_y_position())
        self.move_speed = 0.5
        self.x_step = 10

    @staticmethod
    def get_start_x_position():
        x_position = randint(-280, 280)
        return x_position

    def get_y_position(self):
        global last_y_position
        y_position = randint(-260, 280)

        if last_y_position == y_position:
            return self.get_y_position()

        last_y_position = y_position
        return y_position

    def go_to_new_position(self):
        self.goto(START_X_POSITION, self.get_y_position())

    def move(self):
        if self.xcor() <= -300:
            self.go_to_new_position()
        self.goto(self.xcor() - (self.x_step * self.move_speed), self.ycor())

    def increase_speed(self):
        self.move_speed += 0.3
