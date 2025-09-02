from turtle import Screen, Turtle
import pandas

us_states = pandas.read_csv("50_states.csv")
guessed_states = []

is_game = True
# print(us_states)

screen = Screen()
screen.title("U.S. State Games")
screen.bgpic("blank_states_img.gif")

while is_game:
    user_answer = screen.textinput("U.S. State!", "Type your guess: ")
    if not user_answer:
        is_game = False
        continue
    if user_answer in us_states:
        guessed_states.append(user_answer)
        # add turtle and move to coordinates from cvs of guessed state
    # else
        # maybe add some sort of lives? like 3 attempts to make a wrong answer
        # count down lives num
    # check if lives == 0 -> game is over



screen.exitonclick()
