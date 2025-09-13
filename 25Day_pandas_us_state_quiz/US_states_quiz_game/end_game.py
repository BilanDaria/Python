from turtle import Turtle


class EndGame(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")

    def lose_game(self, points):
        self.write(f"Game Over! Your points: {points}", False, "center", ('Courier', 18, 'normal'))

    def win_game(self):
        self.write(f"You Win! You know all US States!", False, "center", ('Courier', 18, 'normal'))
