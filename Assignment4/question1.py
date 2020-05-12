# Q1: Write a python program to add all the odd numbers from 0 to 20.

from functools import reduce
from collections import deque

is_odd = lambda x: x % 2 == 1


def sum_of_odd(lst):
    # return int(reduce(lambda x, y: x + y if is_odd(y) else x, lst))
    lst = deque(lst)
    lst.appendleft(0)
    # print("Deque : ", list(lst))
    return int(reduce(lambda x, y: x + y if is_odd(y) else x, list(lst)))


def input_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input integers only!")
        num = int(input(msg))
    return num


def generate_list():
    number = input_integer("Please enter desired number of elements : ")
    my_list = list(range(0, number))
    print("List Generated : ", my_list)
    return my_list


def main():
    print("Sum of odd numbers of the list: ", sum_of_odd(generate_list()))


main()
