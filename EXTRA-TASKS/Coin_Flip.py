#!/usr/bin/python3
import random
import sys

aguments = sys.argv
print("Got the arguments: ", len(aguments))
i = 0
while i <= len(aguments):
    print(aguments[i], i)
    i += 1

def Flips(amount):
    Head_or_Tails = 0
    i = 0

    while i <= amount:
        Head_or_Tails = random.randint(0,1)

        if Head_or_Tails == 0:
            print('The flip number: ', i+1, 'The coin landed on HEADS!!!')
        elif Head_or_Tails == 1:
            print('The flip number: ', i+1, 'The coin landed on Tails!!!')

        i += 1


def Argument_Check(aguments):
    if len(aguments) > 2:
        return (print("Too many arguments."))
    elif len(aguments) == 1:
        return (print("Please provide a number of times to flip the coin."))
    elif len(aguments) == 2:
        Flips(aguments[2])


# //////////////////////////// Tests ///////////////////////////
Argument_Check(aguments)
