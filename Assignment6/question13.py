# Q13. Write a Python program to check for a number at the end of a string.

import re


def ends_with_dig(string):
    reg = re.compile(r".*\d$")
    return "YES" if re.match(reg, string) is not None else "NO"


def main():
    string = input("Please input a string : ")
    print("Does your string ends with your digit? ", ends_with_dig(string))


main()
