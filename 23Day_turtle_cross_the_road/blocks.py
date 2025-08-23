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
        self.goto(START_X_POSITION, self.get_to_new_position())
        self.move_speed = 0.1

    def get_to_new_position(self):
        global last_y_position
        new_y_position = randint(-280, 280)

        if last_y_position == new_y_position:
            return self.get_to_new_position()

        last_y_position = new_y_position
        return new_y_position

    def move(self):
        self.goto(self.xcor() + self.move_speed, )
