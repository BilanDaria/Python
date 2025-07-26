from turtle import Turtle, Screen
from random import randint

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -65, -20, 20, 65, 100]
all_turtles = []

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet: ", "Which turtle will win the race? Enter the color: ")

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.up()
    new_turtle.goto(-230, y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
