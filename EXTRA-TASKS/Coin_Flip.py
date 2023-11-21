#!/usr/bin/python3
import random
import sys


print ('\U0001F603')
aguments = sys.argv

def Flips(amount):
    Head_or_Tails = 0
    i = 0

    while i < amount:
        Head_or_Tails = random.randint(0,1)

        if Head_or_Tails == 0:
            print('In the flip number:', i+1, '\n  The coin landed on HEADS!!!\n')
        elif Head_or_Tails == 1:
            print('In the flip number:', i+1, '\n  The coin landed on TAILS!!!\n')

        i += 1


def Argument_Check(aguments):
    if len(aguments) > 2:
        return (print("Too many arguments."))
    elif len(aguments) == 1:
        return (print("Please provide a number of times to flip the coin."))
    elif len(aguments) == 2:
        Flips(int(aguments[1]))


# //////////////////////////// Tests ///////////////////////////
Argument_Check(aguments)
