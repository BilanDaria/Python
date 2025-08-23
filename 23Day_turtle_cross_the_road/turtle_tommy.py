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
        self.start_position()

    def move_up(self):
        if self.heading() != UP:
            self.setheading(UP)
        self.forward(20)

    def move_down(self):
        if self.heading != DOWN:
            self.setheading(DOWN)
        self.forward(20)

    def move_right(self):
        if self.heading != RIGHT:
            self.setheading(RIGHT)
        self.forward(20)

    def move_left(self):
        if self.heading != LEFT:
            self.setheading(LEFT)
        self.forward(20)

    def start_position(self):
        self.setheading(UP)
        self.goto(0, -280)
