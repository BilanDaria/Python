from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Tommy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move_up(self):
        if self.setheading != UP:
            self.setheading(UP)
        self.forward(20)

    def move_down(self):
        if self.setheading != DOWN:
            self.setheading(DOWN)
        self.forward(20)

    def move_right(self):
        if self.setheading != RIGHT:
            self.setheading(RIGHT)
        self.forward(20)

    def move_left(self):
        if self.setheading != LEFT:
            self.setheading(LEFT)
        self.forward(20)
