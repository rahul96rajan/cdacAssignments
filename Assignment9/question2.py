#  Q2: Write a Python Program to find numbers divisible by thirteen from a
# list using anonymous function

from question1 import input_float


def input_positive_integer(msg):
    try:
        num = int(input(msg))
    except ValueError:
        print("Please input positive integers only!")
        num = int(input(msg))
    if num < 0:
        print("Please input positive integers only!")
        num = int(input(msg))
    return num


def input_decimal_list():
    no = input_positive_integer("Enter the desired size of list : ")
    return [input_float("Enter term %d : " % x) for x in range(no)]
    # return [input("Enter term %d : " % x) for x in range(no)]


def main():
    print(input_decimal_list())


main()
