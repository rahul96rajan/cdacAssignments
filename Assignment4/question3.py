# Q3: Write a python program to find the sum of all integers greater than 100 and less than 200.
from functools import reduce


def sum_of_list(lst):
    return int(reduce(lambda x, y: x + y, lst))


def input_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input integers only!")
        num = int(input(msg))
    return num


def generate_list():
    start = input_integer("Please enter starting point of list (ex: 100) : ")
    end = (input_integer("Please enter ending point of list (ex: 200) : ")+1)
    my_list = list(range(start, end))
    print("List Generated :\n=>", my_list)
    return my_list


def main():
    print("Sum of odd numbers of the list: ", sum_of_list(generate_list()))


main()
