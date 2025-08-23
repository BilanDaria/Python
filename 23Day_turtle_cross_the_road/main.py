from time import sleep
from turtle import Screen
from turtle_tommy import Tommy
from blocks import Block
from announcement import Announcement

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle crossing game")
screen.tracer(0)

announcement = Announcement()
tommy = Tommy()

blocks_list = []
blocks_amount = 10
for i in range(blocks_amount):
    block = Block()
    blocks_list.append(block)


screen.listen()
screen.onkeypress(tommy.move_up, "w")
screen.onkeypress(tommy.move_down, "s")
screen.onkeypress(tommy.move_right, "d")
screen.onkeypress(tommy.move_left, "a")

is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.1)

    for i in blocks_list:
        # Detect turtle collision with the block
        if tommy.distance(i) <= 20:
            is_game_on = False
            announcement.game_over()
            break
        i.move()

    # Detect turtle collision with upper edge
    if tommy.ycor() >= 295:
        announcement.new_level()
        tommy.start_position()
        blocks_amount += 5
        for i in blocks_list:
            i.increase_speed()


screen.exitonclick()
