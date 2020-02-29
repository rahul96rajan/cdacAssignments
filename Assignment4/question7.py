# Q7: Display the sum of: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + 1/19 + 1/22 + 1/25

from functools import reduce
from collections import deque


def input_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input integers only!")
        num = int(input(msg))
    return num


def series_total():
    num = input_integer("Please enter a number (ex: 1) : ")
    gap = input_integer("Please enter gap in denominators (ex: 3) : ")
    series_range = (input_integer("Please range required (ex: 10) : "))
    series_sum = 0
    for i in range(0, series_range):
        series_sum += num/(num+(gap*i))
    return series_sum


def main():
    print("Sum of series: ", series_total())


main()