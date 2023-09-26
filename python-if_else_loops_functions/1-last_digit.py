#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = int(str(number)[-1:])
if ldigit > 5:
    print("Last digit of %s is %s and is greater than 5" % (number, ldigit))
elif ldigit == 0:
    print("Last digit of %s is %s and is 0" % (number, ldigit))
else:
    print("Last digit of %s is %s and is less than 6 and not 0" % (number, ldigit))
