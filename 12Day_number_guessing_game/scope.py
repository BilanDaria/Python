# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)

# Global scope
# player_health = 10
#
#
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
#
# drink_potion()
# print(player_health)

# There is no Block Scope
# game_level = 3
#
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemies = enemies[0]
#
#     print(new_enemies)

#Modifying Global Scope
# enemies = "Skeleton"
# enemies = 1
# def increase_enemies():
#     # enemies = "Zombie"
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#     # return enemies
#
# # enemies = increase_enemies()
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global Constants
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"
