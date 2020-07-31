# Q16. Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, MachineLearning exercises, NLP exercises'
# Pattern : 'exercises'
import re


def matching_string_in_string(string1, string2):
    reg = re.compile(string2)
    found = re.finditer(reg, string1)
    if found is None:
        print(string2 + " is not present in " + string1)
    else:
        print(string2 + " is present in " + string1 + " at position(s) =>", *[x.span() for x in found])


def main():
    string1 = input("Please enter a sentence: ")
    string2 = input("Please enter a strings: ")
    matching_string_in_string(string1, string2)


main()
