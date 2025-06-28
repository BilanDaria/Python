############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/
import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
dealer = []

end_the_game = False
is_player = False


def print_current_progress(is_final):
    if not is_final:
        print(f"Your cards: {player}, current score: {sum(player)}")
        print(f"Computer's first card: {dealer[0]}")
        print("------------------------------------------------------")
    else:
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {dealer}, final score: {sum(dealer)}")
        print("------------------------------------------------------")



def check_winner(is_player, current_list, opponent_list):
    if is_player:
        if sum(current_list) == 21:
            print("Win with a Blackjack 😎")
            return True
        elif sum(current_list) > 21:
            print("You went over. You lose 😭")
            return True
        elif sum(current_list) == sum(opponent_list):
            print("Draw 🙃")
            return True
        else:
            return False
    else:
        if sum(current_list) == 21:
            print("Lose, opponent has Blackjack 😱")
            return True
        elif sum(current_list) > 21:
            print("Opponent went over. You win 😁")
            return True
        elif sum(current_list) == sum(opponent_list):
            print("Draw 🙃")
            return True
        elif sum(current_list) < sum(opponent_list):
            print("You win 😃")
            return True
        elif sum(current_list) > sum(opponent_list):
            print("You lose 😤")
            return True
        else:
            return False


def main_logic_of_game(is_player_turn, player_list, computer_list):
    should_exit = False
    end_of_computer_turn = False
    while not should_exit:
        is_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if is_continue == 'y':
            player_list.append(random.choice(cards))
            print_current_progress(False)
            should_exit = check_winner(is_player_turn, player_list, computer_list)
            if should_exit:
                print_current_progress(True)
                return True     # ?
            else:
                continue
        elif is_continue == 'n':
            while not end_of_computer_turn:
                if sum(computer_list) < 17:
                    computer_list.append(random.choice(cards))
                else:
                    is_player_turn = False
                    end_of_computer_turn = check_winner(is_player_turn, computer_list, player_list)
                    if end_of_computer_turn:
                        print_current_progress(True)
                        return True     # ?
                    else:
                        continue

################## Start ##################

print(logo)

while True:
    start_game = input("~ Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    print("------------------------------------------------------")

    if start_game == 'y':
        player = [random.choice(cards)]
        if player[0] == 11:
            el = random.choice(cards)
            if el == 11:
                player.append(1)
            else:
                player.append(random.choice(cards))
        else:
            player.append(random.choice(cards))

        dealer = [random.choice(cards)]
        if dealer[0] == 11:
            el = random.choice(cards)
            if el == 11:
                dealer.append(1)
            else:
                dealer.append(random.choice(cards))
        else:
            dealer.append(random.choice(cards))

        print_current_progress(False)
        if sum(player) == 21:
            print("Wow, you win from the beginning! You are a lucky guy ✨")
            continue
        else:
            is_player = True
            main_logic_of_game(is_player, player, dealer)
            clear()
            continue
    elif start_game == 'n':
        break
    else:
        print("Invalid input. Restart the program and try again!")
        

