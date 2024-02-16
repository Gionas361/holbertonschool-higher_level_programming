#!/usr/bin/python3
import random
import sys


aguments = sys.argv

def Flips(amount):
    # Prints the guide to reading the results
    print("Heads = \U0001F31D")
    print("Tails = \U0001F31A")
    print("\n")

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
        return (print("\n# Too many arguments.\n"))
    elif len(aguments) == 1:
        return (print("\n# Please provide a number of times to flip the coin.\n"))
    elif len(aguments) == 2 and int(aguments[1]) <= 0:
        return (print('\n# Please provide a positive number.\n'))
    elif len(aguments) == 2 and aguments[1] != '--help':
        Flips(int(aguments[1]))
    elif (aguments[1] == '--help'):
        print('\n# To use this file just write a number after the executable,')
        print('# this will determine how many times to flip the coin.\n')
        return(None)


# //////////////////////////// Tests ///////////////////////////
Argument_Check(aguments)
