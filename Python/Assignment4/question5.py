# Q5: Write a program to display the sum of square of the first ten even natural numbers

from functools import reduce
from collections import deque


def squared_sum_of_list(lst):
    lst = deque(lst)
    lst.appendleft(0)
    return int(reduce(lambda x, y: x + (y**2), lst))


def input_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input integers only!")
        num = int(input(msg))
    return num


def generate_list():
    start = input_integer("Please enter starting point of list (ex: 1) : ")
    end = (input_integer("Please enter ending point of list (ex: 10) : ")+1)
    my_list = list(range(start, end))
    print("List Generated :\n=>", my_list)
    return my_list


def main():
    print("Sum of squares of the list: ", squared_sum_of_list(generate_list()))


main()
