from turtle import Screen, Turtle
import pandas

from state_name import StateName

us_states = pandas.read_csv("50_states.csv")
us_states_list = us_states.state.to_list()  # useless
guessed_states = []

is_game = True
user_lives = 3

screen = Screen()
screen.title("U.S. State Games")
screen.bgpic("blank_states_img.gif")

while is_game:
    user_answer = screen.textinput("U.S. State!", "Type your guess: ")
    print("i'm here")
    if not user_answer:
        is_game = False
        print("bad")
        continue

    if user_answer.capitalize() in us_states.state.values:
        state_name = us_states[us_states.state == user_answer.capitalize()].state.values[0]
        state_x_coord = us_states[us_states.state == user_answer.capitalize()].x.values[0]
        state_y_coord = us_states[us_states.state == user_answer.capitalize()].y.values[0]
        state = StateName(state_name, state_x_coord, state_y_coord)
        guessed_states.append(state)
        state.set_title_position()
    else:
        user_lives -= 1
        if user_lives <= 1:


        # maybe add some sort of lives? like 3 attempts to make a wrong answer
        # count down lives num
    # check if lives == 0 -> game is over



screen.exitonclick()
