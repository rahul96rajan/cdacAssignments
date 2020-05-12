# Q14. Write a Python program to search the numbers (0-9) of length
# between 1 to 3 in a given string.
import re


def matching_seq(string):
    reg = re.compile(r"\d{1,3}")
    return [x.group() for x in re.finditer(reg, string)]


def main():
    string = input("Please enter a sentence: ").strip()
    print("Matching Sequences : ", matching_seq(string))


main()
