from turtle import Turtle
MOVE_DISTANCE = 20
LEFT_X_COORD = -370

class Paddle:
    def __init__(self, start_position):
        self.paddle_segment = []
        self.create_paddle(start_position)
        self.first_segment = self.paddle_segment[0]
        self.last_segment = self.paddle_segment[-1]

    def create_paddle(self, start_positions):
        for i in start_positions:
            new_segment = Turtle("square")
            new_segment.up()
            new_segment.color("white")
            new_segment.goto(i)
            new_segment.setheading(90)
            self.paddle_segment.append(new_segment)

    def move_up(self):
        for i in range(len(self.paddle_segment) - 1, 0, -1):
            new_x = LEFT_X_COORD
            new_y = self.paddle_segment[i - 1].ycor()
            self.paddle_segment[i].goto(new_x, new_y)
        self.first_segment.forward(MOVE_DISTANCE)


