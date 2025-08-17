from turtle import Turtle
MOVE_DISTANCE = 20
LEFT_X_COORD = -370
UP = 90
DOWN = 270


class Paddle:
    def __init__(self, start_position, x_coord):
        self.paddle_segment = []
        self.create_paddle(start_position)
        self.x_coord = x_coord
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

    def move(self):
        for i in range(len(self.paddle_segment) - 1, 0, -1):
            # print(f'im here {self.paddle_segment[i].ycor()}')
            new_x = self.x_coord
            new_y = self.paddle_segment[i - 1].ycor()
            self.paddle_segment[i].goto(new_x, new_y)
        self.first_segment.forward(MOVE_DISTANCE)
        return True

    def up(self):
        if self.first_segment.ycor() == 280.00:
            print("it's end here")
            return False

        if self.first_segment.heading() != UP:
            self.first_segment.setheading(UP)

        return self.move()

    def down(self):
        if self.first_segment.ycor() == -280.00:
            print("it's end here")
            return False

        if self.first_segment.heading() != DOWN:
            self.first_segment.setheading(DOWN)

        return self.move()
