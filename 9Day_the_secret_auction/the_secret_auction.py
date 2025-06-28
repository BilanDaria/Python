from replit import clear
from art import logo

auction = {}
is_going = True
answ = ""


def add_bid_record(person, bid_amount):
    auction[person] = bid_amount


def get_winner():
    max_bid = -1
    winner = ""
    for i in auction:
        if auction.get(i, 0) > max_bid:
            max_bid = auction.get(i, 0)
            winner = i
        else:
            continue
    return f"The winner is {winner} with a bid ${max_bid}!"


print(logo)

while is_going:
    name = input("What is your name? : ")
    bid = float(input("What is your bid? : "))
    add_bid_record(name, bid)

    answ = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
    if answ == 'yes':
        clear()
    elif answ == 'no':
        is_going = False
        print(get_winner())
    else:
        print("Invalid input data! Good buy loser!")
        break

# print(auction)


