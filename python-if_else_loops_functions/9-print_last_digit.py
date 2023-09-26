#!/usr/bin/python3
def print_last_digit(number):
    if number is int:
        number = str(number)
    number = int(str(number)[-1:])
    print(number, end="")
    return(number)
