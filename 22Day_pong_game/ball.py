from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("white")
        self.x_move_step = 5
        self.y_move_step = 5
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move_step, self.ycor() + self.y_move_step)

    def bounce_y(self):
        self.y_move_step *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move_step *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.bounce_y()
        self.move_speed = 0.1


