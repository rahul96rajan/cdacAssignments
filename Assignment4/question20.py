# Q20. Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

from re import split
from collections import Counter


def input_comma_separated_list():
    list_string = input("Please enter a string: ").strip()
    lst = split("\s+", list_string)
    print("\n"+'\033[1m'+ '\033[4m' + "String : Count" + '\033[0m')
    for x, y in Counter(lst).items():
        print(x, " : ", y)


input_comma_separated_list()
