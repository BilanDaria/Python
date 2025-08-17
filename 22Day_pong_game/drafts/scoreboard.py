from turtle import Turtle
FONT = ('Arial', 8, 'normal')

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.setpos(position)
        self.setheading(90)
        self.pensize(5)

    def line(self):
        while self.ycor() <= 345:
            self.forward(30)
            self.pendown()
            self.forward(30)
            self.penup()

    def increase_score(self):
        self.score += 1

    def score_counter_update(self, align):
        self.clear()
        self.write(arg=self.score, move=False, align=align.lower(), font=FONT) # type error for align
