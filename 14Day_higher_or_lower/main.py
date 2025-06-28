# TODO 1 import arts and game items list + random
from art import logo, vs
from game_data import data
from random import choice
from replit import clear


# Get item B
def get_itemB(item2):
    item1 = choice(data)
    while True:
        if item1 == item2:
            item1 = choice(data)
            continue
        else:
            break
    return item1


# Print comparison items
def print_items(a, b):
    print(f"Compare A: {a.get('name')}, {a.get('description')}, from {a.get('country')}")
    print(vs)
    print(f"Against B: {b.get('name')}, {b.get('description')}, from {b.get('country')}")


# Print result of round
def print_final_result(points, is_win):
    if is_win:
        clear()
        print(f"You're right! Current score: {points}.")
    else:
        clear()
        print(f"Sorry, that's wrong! Final score: {points}")


# TODO 5. method for comparing num of followers
def comparing_followers(user_choice, a_followers, b_followers, points):
    if a_followers == b_followers:
        print("Oops, they have same number of followers. We give u +1 point anyway 😉")
        points += 1
        return points
    elif a_followers > b_followers:
        if user_choice.lower() == 'a':
            points += 1
            print_final_result(points, True)
            return points
        else:
            print_final_result(points, False)
            return 0
    else:
        if user_choice.lower() == 'b':
            points += 1
            print_final_result(points, True)
            return points
        else:
            print_final_result(points, False)
            return 0

# Else way of comparing
    # elif user_choice == 'a':
    #     if a_followers > b_followers:
    #         points += 1
    #         return points
    #     else:
    #         return 0
    # else:
    #     if a_followers < b_followers:
    #         points += 1
    #         return points
    #     else:
    #         return 0


# TODO 2 initiate variables score - int, is_fail - bool, A - for first element, B - for second element
# TODO 3 use choice to get info for A and B. UPD: make a method to generate new B
# TODO 6. Main game block
def start_game():
    score = 0
    is_fail = False
    item_a = choice(data)

    while not is_fail:
        item_b = get_itemB(item_a)
        print_items(item_a, item_b)
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        # print(answer)
        if answer == 'a' or answer == 'b':
            score = comparing_followers(answer, item_a.get('follower_count'), item_b.get('follower_count'), score)
            if score > 0:
                item_a = item_b
                continue
            else:
                is_fail = True
                continue
        else:
            print_final_result(score, False)
            break


# TODO 4. Print enter block + start the game
############ MAIN #############
print(logo)
start_game()


