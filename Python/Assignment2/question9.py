# Question 9: Write a Python program to get the least common multiple (LCM) of two positive integers.

from math import gcd


def is_positive(num):
    if num > 0:
        return True
    else:
        return False


def input_positive_int(msg):
    try:
        num = int(input(msg))
        if not (is_positive(num)):
            num = int(input(msg))
    except ValueError:
        num = int(input(msg))
    return num


def lcm(num1, num2):
    return (num1*num2)/gcd(num1, num2)


def main():
    num1 = input_positive_int("Please enter number 1 (positive integer):")
    num2 = input_positive_int("Please enter number 2 (positive integer):")
    print("LCM => ", lcm(num1, num2))


main()
