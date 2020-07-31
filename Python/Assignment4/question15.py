# Q15: write a Python program to check if the input number is prime or not.

from math import factorial


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


def wilson_s_formula(num):
    return True if factorial(num-1)%num == (num-1) else False


def main():
    num = input_positive_integer("Enter a value: ")
    print("Prime => ", wilson_s_formula(num))


main()