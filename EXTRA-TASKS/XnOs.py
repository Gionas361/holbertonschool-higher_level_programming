#!/usr/bin/python3
import random
import sys


# Variables containin the emojis the guide to reading the results
# Results
Win = "\U0001F31D" # Not gonna be used lmao
Loss = "\U0001F31A"
Tie = "\U0001F501"

# Moves for players
Boxes = "\U0001F532"
X = "\U0001F380"
O = "\U0001F4C0"

# Array of play
Table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
i = 0
x = 0
while i < 3:
    while x < 3:
        Table[i][x] = Boxes
        print(Table[i][x], end = " ")
        x += 1
    print()
    i += 1
    x = 0

def TurnPlayouts():
    turn = 0

    if turn == 0:
        p