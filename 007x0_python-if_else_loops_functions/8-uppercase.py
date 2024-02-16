#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if c >= chr(97) and c <= chr(122):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
