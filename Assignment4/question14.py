# Q14: write a Python program to find the factorial of a number provided by the user
from functools import reduce


def input_positive_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input positive integers only!")
        num = int(input(msg))
    if num < 0:
        print("Please input positive integers only!")
        num = int(input(msg))
    return num


def factorial():
    num = input_positive_integer("Please enter a positive integer: ")
    print("%d! = "% num, int(reduce(lambda x, y: x * y, range(1, num + 1))))


factorial()
