#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = int(str(number)[-1:])
number = int(number)
print("Last digit of ", end="")
if number < 0:
    ldigit = -ldigit
if ldigit > 5:
    print("{} is {} and is greater than 5".format(number, ldigit))
elif ldigit == 0:
    print("{} is {} and is 0".format(number, ldigit))
else:
    print("{} is {} and is less than 6 and not 0".format(number, ldigit))
