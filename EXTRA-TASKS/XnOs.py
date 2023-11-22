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

# Array with win positions
Wpos = [['0', '1', '2'], ['10', '11', '12'], ['20', '21', '22'],
        ['0', '10', '20'], ['1', '11', '21'], ['2', '12', '22'],
        ['2', '11', '20'], ['0', '11', '22']]

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

def CPU_AI(gameturn, mode):
    # Variable declaration

    location1 = 0
    location2 = 0
    location = 0

    curTab = [[69, 69], [69, 69], [69, 69],
              [69, 69], [69, 69], [69, 69],
              [69, 69], [69, 69], [69, 69]]
    foundpath = [0, 0]
    c1 = 0
    c2 = 0

    addit = 0
    i = 0
    x = 0
    w = 0
    p = 0
    c = 0

    # They will check for the turn and act acordingly
    if gameturn == 3:
        mode = 0
        if (Table[0][1] == Xs or Table[1][0] == Xs or Table[1][2] == Xs or Table[2][1] == Xs):
            # Win mode activate
            mode = 'WIN'

            # It will select one of the positions besides the one that the player chose
            if Table[0][1] == Xs:
                location = random.randint(0,1)
                if location == 0:
                    Table[0][0] = Os
                if location == 1:
                    Table[0][2] = Os
            if Table[1][0] == Xs:
                location = random.randint(0,1)
                if location == 0:
                    Table[0][0] = Os
                if location == 1:
                    Table[2][0] = Os
            if Table[1][2] == Xs:
                location = random.randint(0,1)
                if location == 0:
                    Table[0][2] = Os
                if location == 1:
                    Table[2][2] = Os
            if Table[2][1] == Xs:
                location = random.randint(0,1)
                if location == 0:
                    Table[2][0] = Os
                if location == 1:
                    Table[2][2] = Os

        if (Table[0][0] == Xs or Table[0][2] == Xs or Table[2][0] == Xs or Table[2][2] == Xs):
            # Tie mode activate
            openslot = 0
            mode = 'TIE'

            # It will result in CPU choosing any random position not already taken,
            # if it is taken it will just generate another slot to play in.
            while openslot != 1:
                location1 = random.randint(0,2)
                location2 = random.randint(0,2)

                if (Table[location1][location2] == Boxes):
                    Table[location1][location2] = Os
                    openslot = 1
    
    # Turn 5 actions
    if gameturn == 5:
        if mode == 'WIN':

            # It will store where each player has put a mark
            while i < 3:
                while x < 3:
                    if Table[i][x] != Boxes:
                        curTab[c1][c2] = int(f'{i}{x}')
                        curTab[c1][c2+1] = Table[i][x]
                    c1 += 1
                    x += 1
                i += 1
                x = 0

            # This determines if the player fucked up and if they did,
            # it will play the move that will win him the game.
            while w < 8: # Sets of 3 for victory
                print(f'w: {w}')
                addit = 0
                while p < 3: # Nums inside the sets
                    print(f'p: {p}')
                    while c < 9:
                        print(f'c: {curTab[c][c2]} {Wpos[w][p]}')
                        if (int(curTab[c][c2]) == int(Wpos[w][p])):
                            if curTab[c][c2+1] != Xs:
                                addit += 1
                            else:
                                addit -= 1
                            print(f'addit: {addit}')
                        c += 1
                    p += 1
                    c = 0
                    if addit == 2:
                        print('it was noticed')
                        p = 0
                        while p < 3:
                            if int(p) < 10:
                                foundpath[0] = 0
                                foundpath[1] = Wpos[w][p]
                                print('yesy', foundpath[0], foundpath[1])
                            else:
                                foundpath = [int(i) for i in str(Wpos[w][p])]
                                print('nopy', foundpath[0], foundpath[1])
                            Table[int(foundpath[0])][int(foundpath[1])] = Os
                            p += 1
                w += 1
                p = 0

    return (mode)



def Turn_Playouts():
    turn = 1
    gameend = 0
    gameturn = 1
    mode = 0

    while gameend == 0:
        gameturn += 1

        if turn == 0:
            print(f"It's the cpu's turn: [{gameturn}] {mode}")
            mode = CPU_AI(gameturn, mode)
            PrintOutTable()
            gamened = Win_Check()

            turn = 1
        elif turn == 1:
            print(f"It's the player's turn: [{gameturn}] {mode}")
            Turn_Check()
            PrintOutTable()
            gameend = Win_Check()

            turn = 0

# /////////////////////////////// Tests ///////////////////////////////////
# First turn always goes to cpu
Table[1][1] = Os
PrintOutTable()
Turn_Playouts()