# Q20. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
import re


def abbreviate(string):
    rd = re.compile("Road", re.IGNORECASE)
    string = rd.sub("Rd", string)
    return string


def main():
    string = input("Please input a string : ")
    print("After abbreviation : ", abbreviate(string))


main()
