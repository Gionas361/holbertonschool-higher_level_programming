#!/usr/bin/python3
import random
import sys


# Prints the guide to reading the results
print("Heads = \U0001F31D")
print("Tails = \U0001F31A")
print("\n")
aguments = sys.argv

def Flips(amount):
    # It will print each coin flip based on
    # the number provided but Argument_Check.

    Head_or_Tails = 0
    i = 0

    while i < amount:
        Head_or_Tails = random.randint(0,1)

        if Head_or_Tails == 0:
            print('The coin number', i+1, 'landed on \U0001F31D')
        elif Head_or_Tails == 1:
            print('The coin number', i+1, 'landed on \U0001F31A')

        i += 1


def Argument_Check(aguments):
    # It will check that a number is provided.

    if len(aguments) > 2:
        return (print("Too many arguments."))
    elif len(aguments) == 1:
        return (print("Please provide a number of times to flip the coin."))
    elif len(aguments) == 2:
        Flips(int(aguments[1]))


# //////////////////////////// Tests ///////////////////////////
Argument_Check(aguments)
