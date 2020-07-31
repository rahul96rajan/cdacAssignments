# Q3. Write a Python program to find all five characters long word in a string.
import re


def fetch_string(string):
    reg = re.compile(r"\b\w{5}\b")
    return re.findall(reg, string)


def main():
    string = input("Please input a string : ")
    print("Five letter words in the string are :\n =>", fetch_string(string))


main()
