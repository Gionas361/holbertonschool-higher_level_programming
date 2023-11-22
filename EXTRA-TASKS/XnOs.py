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
for i in Table:
    for x in i:
        Table[i][x] = Boxes
        print(x, end = " ")
    print()

def TurnPlayouts():
    turn = 0

    if turn == 0:
        p