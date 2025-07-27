from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.hideturtle()
        self.setposition(0, 278)
        self.color("white")
        self.update_the_scoreboard()

    def update_the_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)

    def increase_points(self):
        self.points += 1
        self.update_the_scoreboard()
