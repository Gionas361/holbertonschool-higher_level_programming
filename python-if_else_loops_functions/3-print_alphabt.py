#!/usr/bin/python3
letter = 97
while letter < 123:
    if letter == 113 or letter == 101:
        letter = letter + 1
    else:
        print("{}".format(chr(letter)), end="")
        letter = letter + 1
