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
Xs = "\U0001F380"
Os = "\U0001F4C0"

# Array for storing arguments
aguments = [0, 0]

# Array of play / Reseting board
Table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
i = 0
x = 0
while i < 3:
    while x < 3:
        Table[i][x] = Boxes
        x += 1
    i += 1
    x = 0

# Functions:
def PrintOutTable():
    i = 0
    x = 0
    while i < 3:
        while x < 3:
            print(Table[i][x], end = " ")
            x += 1
        print()
        i += 1
        x = 0

def Turn_Check():
    # It will receive input first and then,
    # It will check that the numbers provided are correct.
    # If they are it will return a column and row.
    openslot = 0

    while openslot != 1:
        print("What column would u like to play in?")
        aguments[0] = int(input())
        print("What row would u like to play in?")
        aguments[1] = int(input())

        if ((aguments[0] > 3 and aguments[0] < 0) and (aguments[1] > 3 and aguments[1] < 0)):
            print("Please provide values in the range of 1 and 3.\n")
        if (Table[aguments[1]-1][aguments[0]-1] == Boxes):
            Table[aguments[1]-1][aguments[0]-1] = Xs
            openslot = 1
        elif (Table[aguments[1]-1][aguments[0]-1] != Boxes):
            print("Please select an unocupied slot.")

    # If the number of arguments is the correct amount:
    return (int(aguments[0]), int(aguments[1]))

def Win_Check():
    if (
       # Horizontals
       ((Table[0][0] == Os) and (Table[0][1] == Os) and (Table[0][2] == Os)) or
       ((Table[1][0] == Os) and (Table[1][1] == Os) and (Table[1][2] == Os)) or
       ((Table[2][0] == Os) and (Table[2][1] == Os) and (Table[2][2] == Os)) or
       # Verticals
       ((Table[0][0] == Os) and (Table[1][0] == Os) and (Table[2][0] == Os)) or
       ((Table[0][1] == Os) and (Table[1][1] == Os) and (Table[2][1] == Os)) or
       ((Table[0][2] == Os) and (Table[1][2] == Os) and (Table[2][2] == Os)) or
       # Diagonals
       ((Table[0][2] == Os) and (Table[1][1] == Os) and (Table[2][0] == Os)) or
       ((Table[0][0] == Os) and (Table[1][1] == Os) and (Table[2][2] == Os))
       ):
       print("CPU WINS!!!")
       return (1)

    if (
       # Horizontals
       ((Table[0][0] == Xs) and (Table[0][1] == Xs) and (Table[0][2] == Xs)) or
       ((Table[1][0] == Xs) and (Table[1][1] == Xs) and (Table[1][2] == Xs)) or
       ((Table[2][0] == Xs) and (Table[2][1] == Xs) and (Table[2][2] == Xs)) or
       # Verticals
       ((Table[0][0] == Xs) and (Table[1][0] == Xs) and (Table[2][0] == Xs)) or
       ((Table[0][1] == Xs) and (Table[1][1] == Xs) and (Table[2][1] == Xs)) or
       ((Table[0][2] == Xs) and (Table[1][2] == Xs) and (Table[2][2] == Xs)) or
       # Diagonals
       ((Table[0][2] == Xs) and (Table[1][1] == Xs) and (Table[2][0] == Xs)) or
       ((Table[0][0] == Xs) and (Table[1][1] == Xs) and (Table[2][2] == Xs))
       ):
       print("PLAYER WINS!!!")
       return (1)
    
    return (0)

def CPU_AI(gameturn):
    location1 = 0
    location2 = 0

    if gameturn == 3:
        if (Table[0][1] == Xs or Table[1][0] == Xs or Table[1][2] == Xs or Table[2][1]):
            # Win mode activate
            openslot = 1

            while openslot != 1:
                location1 = random.randint(0,1)
                if location1 == 1:
                    location1 == 2
                location2 = random.randint(0,1)
                if location2 == 1:
                    location2 == 2

                if (Table[location1][location2] == Boxes):
                    Table[location1][location2] = Os
                    openslot = 1
            

        if (Table[0][0] == Xs or Table[0][2] == Xs or Table[2][0] == Xs or Table[2][2]):
            # Tie mode activate
            openslot = 0

            while openslot != 1:
                location1 = random.randint(0,2)
                location2 = random.randint(0,2)

                if (Table[location1][location2] == Boxes):
                    Table[location1][location2] = Os
                    openslot = 1

def Turn_Playouts():
    turn = 1
    gameend = 0
    gameturn = 1

    while gameend == 0:
        gameturn += 1

        if turn == 0:
            print(f"It's the cpu's turn: [{gameturn}]")
            CPU_AI(gameturn)
            PrintOutTable()
            gamened = Win_Check()

            turn = 1
        elif turn == 1:
            print(f"It's the player's turn: [{gameturn}]")
            Turn_Check()
            PrintOutTable()
            gameend = Win_Check()

            turn = 0

# /////////////////////////////// Tests ///////////////////////////////////
# First turn always goes to cpu
Table[1][1] = Os
PrintOutTable()
Turn_Playouts()