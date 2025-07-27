from turtle import Turtle


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
            self.paddle_segment.append(new_segment)

    def get_position(self):
        for i in self.paddle_segment:
            print(i.position())

test = Paddle([(-285, 20), (-285, 0), (-285, -20)])
print(test.get_position())
