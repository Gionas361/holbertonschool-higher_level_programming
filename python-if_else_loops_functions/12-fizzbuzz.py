#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if ((num % 3) == 0):
            print("Fizz", end="")
        if ((num % 5) == 0):
            print("Buzz", end="")
        if ((num % 3) != 0) and ((num % 5) != 0):
            print("{}".format(num), end="")
        if (num != 100):
            print(" ", end="")
        num = num + 1
