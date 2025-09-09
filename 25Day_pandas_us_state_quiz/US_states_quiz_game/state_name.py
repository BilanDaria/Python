from turtle import Turtle
class StateName(Turtle):
    def __init__(self, name, x_coord, y_coord):
        super().__init__()
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.penup()
        self.color("black")
        self.hideturtle()

    def set_title_position(self):
        self.setposition(self.x_coord, self.y_coord)
        self.write(self.name, False, "center", ('Courier', 18, 'normal'))



