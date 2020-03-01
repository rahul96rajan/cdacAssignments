# Q6. Write a Python program to find sequences of lowercase letters joined with
# a underscore.
import re


def matching_seq(string):
    reg = re.compile("_[a-z]_")
    return re.findall(reg, string)


def main():
    string = input("Please enter a sentence: ").strip()
    print("Matching Sequences : ", matching_seq(string))


main()
