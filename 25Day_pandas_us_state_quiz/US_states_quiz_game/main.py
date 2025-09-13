from turtle import Screen, Turtle
import pandas

from state_name import StateName
from end_game import EndGame

us_states = pandas.read_csv("50_states.csv")
us_states_list = us_states.state.to_list()
guessed_states = []

is_game = True
user_lives = 3
win_points = 0

end_game = EndGame()

screen = Screen()
screen.title("U.S. State Games")
screen.bgpic("blank_states_img.gif")


def get_user_answer():
    answer = screen.textinput("U.S. State!", "Type your guess: ").title()
    if not answer or answer == "Exit":
        return
    return answer


def check_user_answer(answer, win_points, user_lives):

    if user_answer not in us_states.state.values:
        user_lives -= 1
        return user_lives, win_points

    win_points += 1
    state = show_guessed_state(answer)
    guessed_states.append(state)
    us_states_list.remove(answer)
    return user_lives, win_points


def show_guessed_state(answer):
    row = us_states[us_states.state == answer]
    state_name = row.state.values[0]
    state_x_coord = row.x.values[0]
    state_y_coord = row.y.values[0]
    state = StateName(state_name, state_x_coord, state_y_coord)
    state.set_title_position()
    return state


while is_game:
    user_answer = get_user_answer()
    if not user_answer:
        is_game = False
        continue

    user_lives, win_points = check_user_answer(user_answer, win_points, user_lives)
    if user_lives == 0:
        end_game.lose_game(win_points)
        is_game = False
        continue

    if len(us_states_list) == 0:
        end_game.win_game()
        is_game = False


screen.exitonclick()
