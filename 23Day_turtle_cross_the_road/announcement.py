from turtle import Turtle


class Announcement(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1

    def game_over(self):
        self.write("GAME OVER!", align="center", font=("Courier", 60, "normal"))

    def new_level(self):
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 60, "normal"))
        self.getscreen().ontimer(self.clear, 1000)

    # def clear_info(self):
    #     self.clear()
