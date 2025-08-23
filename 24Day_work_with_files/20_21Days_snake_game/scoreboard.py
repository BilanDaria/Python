from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.setposition(0, 278)
        self.color("white")
        self.update_the_scoreboard()

    def update_the_scoreboard(self):
        self.clear()
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.write(f"Your Score: {self.score} High score: {self.high_score}", False, ALIGNMENT, FONT)

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write(f"GAME OVER", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_the_scoreboard()

    def increase_points(self):
        self.score += 1
        self.update_the_scoreboard()
