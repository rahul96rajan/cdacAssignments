# Q7. Write a Python program to split a string at uppercase letters.
import re


def fetch_string(string):
    reg = re.compile(r"[A-Z]")
    return re.split(reg, string)


def main():
    string = input("Please input a string : ")
    print("List after splitting string :\n =>", fetch_string(string))


main()
