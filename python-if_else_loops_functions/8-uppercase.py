#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if chr(c) >= 97 and chr(c) <= 122:
            c = chr(chr(c) - 32)
        print("{}".format(c), end="")
    print("")
