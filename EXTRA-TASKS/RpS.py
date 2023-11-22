#!/usr/bin/python3
import random
import sys


# Variables containin the emojis the guide to reading the results
Win = "\U0001F31D"
Loss = "\U0001F31A"
Tie = "\U0001F501"
Scissor = "\U0001F52A"
Paper = "\U0001F4DC"
Rock = "\U0001F48E"
aguments = sys.argv

def RockPaperCut(amount, player):
    # It will print each coin flip based on
    # the number provided but Argument_Check.

    i = 0

    while i < amount:
        Hand = random.randint(0,2)

        # Losses
        if Hand == 0 and player == 'ROCK':
            print(f"The CPU played {Paper}  You played {Rock}. You've {Loss}")
        elif Hand == 1 and player == 'SCISSOR':
            print(f"The CPU played {Rock}  You played {Scissor}. You've {Loss}")
        elif Hand == 2 and player == 'PAPER':
            print(f"The CPU played {Scissor}  You played {Paper}. You've {Loss}")

        # Wins
        elif Hand == 0 and player == 'SCISSOR':
            print(f"The CPU played {Paper}  You played {Scissor}. You've {Win}")
        elif Hand == 1 and player == 'PAPER':
            print(f"The CPU played {Rock}  You played {Paper}. You've {Win}")
        elif Hand == 2 and player == 'ROCK':
            print(f"The CPU played {Scissor}  You played {Rock}. You've {Win}")

        # Ties
        elif Hand == 0 and player == 'Paper':
            print(f"The CPU played {Paper}  You played {Paper}. It's a {Tie}")
        elif Hand == 1 and player == 'ROCK':
            print(f"The CPU played {Rock}  You played {Rock}. It's a {Tie}")
        elif Hand == 2 and player == 'ROCK':
            print(f"The CPU played {Scissor}  You played {Scissor}. It's a {Tie}")

def Argument_Check(aguments):
    # It will check that a number is provided.

    if len(aguments) > 3:
        return (print("Too many arguments."))
    elif len(aguments) < 3:
        return (print("Please provide the number of times to run the game and hand you will use against CPU."))
    elif len(aguments) == 3:
        # If the number of arguments is the correct amount,
        # We create the array of words and then check if,
        # the word given is Rock, Paper or Scissors.
        print("Detected correct amount of arguments.")

        i = 0
        words = ['ROCK', 'SCISSOR', 'PAPER']

        while i <= len(words):
            if aguments[1].upper() == words[i]:
                RockPaperCut(int(aguments[1]), aguments[2].upper())
        print("Please provide a valid word:\n    Rock\n    Paper\n    Scissors\n")

# //////////////////////////// Tests ///////////////////////////
Argument_Check(aguments)
