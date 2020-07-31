# Q7. Write a Python program to find the sequences of
# one upper case letter followed by lower case letters.

import re


def matching_seq(string):
    reg = re.compile("[a-z][A-Z]")
    return re.findall(reg, string)


def main():
    string = input("Please enter a sentence: ").strip()
    print("Matching Sequences : ", matching_seq(string))


main()
