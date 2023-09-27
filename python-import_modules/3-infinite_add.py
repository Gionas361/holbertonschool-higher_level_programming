#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0
    arg = 0
    currarg = 0
    count = len(sys.argv) - 1

    for i in range(count):
        arg = arg + 1
        result = int(result) + int(sys.argv[arg])
    print("{}".format(result))
