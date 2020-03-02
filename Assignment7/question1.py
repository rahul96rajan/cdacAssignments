# Q1. Write a Python program to replace all occurrences of
# space, comma, or dot with a colon.
import re


def replace_string(string):
    reg = re.compile(r"[\s,\.]")
    return re.sub(reg, ":", string)


def main():
    string = input("Please input a string : ")
    print("Replaced String : ", replace_string(string))


main()
