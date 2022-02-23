print("Starting game up...")

import time




game = [
    ["", "", ""],
    ["", "+", ""],
    ["", "", ""]
]


def init():
    for i in range(len(game)):
        print(game[i])


find_in_list_of_list(game, "+")

# import pygame
time.sleep(2)

# while True:
init()
#    direct = str(input("What direction( Up(u), down(d), left(l) or right(r))? "))
#    if direct == "u":
#       up()
