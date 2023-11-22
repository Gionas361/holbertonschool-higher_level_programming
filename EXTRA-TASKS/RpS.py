#!/usr/bin/python3
import random
import sys


# Variables containin the emojis the guide to reading the results
Win = "\U0001F31D"
Loss = "\U0001F31A"
Scissor = "\U0002702"
Paper = "\U0001F4DC"
Rock = "\U0001F48E"
aguments = sys.argv

def RockPaperCut(player):
    # It will print each coin flip based on
    # the number provided but Argument_Check.
    print("Ran RockPaperCut.")

    Hand = random.randint(0,2)

    if Hand == 0 and player == 'ROCK':
        print(f"The CPU played {Paper} you played {Rock}. You've {Loss}")
    elif Hand == 1 and player == 'SCISSOR':
        print(f"The CPU played {Rock} you played {Scissor}. You've {Loss}")
    elif Hand == 2 and player == 'PAPER':
        print(f"The CPU played {Scissor} you played {Paper}. You've {Loss}")
    elif Hand == 0 and player == 'SCISSOR':
        print(f"The CPU played {Paper} you played {Scissor}. You've {Win}")
    elif Hand == 1 and player == 'PAPER':
        print(f"The CPU played {Rock} you played {Paper}. You've {Win}")
    elif Hand == 2 and player == 'ROCK':
        print(f"The CPU played {Scissor} you played {Rock}. You've {Win}")
    
    sys.argv = ''


def Argument_Check(aguments):
    # It will check that a number is provided.
    print("Ran Argument_Check.")

    if len(aguments) > 2:
        return (print("Too many arguments."))
    elif len(aguments) == 1:
        return (print("Please provide the hand you will use against CPU."))
    elif len(aguments) == 2:
        # If the number of arguments is the correct amount,
        # We create the array of words and then check if,
        # the word given is Rock, Paper or Scissors.
        print("Detected correct amount of arguments.")

        i = 0
        words = ['ROCK', 'SCISSOR', 'PAPER']
        print("Created the array.")

        while i <= len(words):
            if aguments[1].upper() == words[i]:
                RockPaperCut(aguments[1].upper())
        print("Please provide a valid word:\n    Rock\n    Paper\n    Scissors\n")

# //////////////////////////// Tests ///////////////////////////
Argument_Check(aguments)
