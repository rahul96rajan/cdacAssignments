# Q5. Write a Python program to find all words which are at least
# 4 characters long in a string.
import re


def fetch_string(string):
    reg = re.compile(r"\b\w{1,4}\b")
    return re.findall(reg, string)


def main():
    string = input("Please input a string : ")
    print("At least 4 chars words in the string are :\n =>", fetch_string(string))


main()
