# Q10. Write a Python program to match a string that
# contains only upper and lowercase letters, numbers, and underscores.

import re


def matching_seq(string):
    reg = re.compile(r"^\w+$")
    return "Condition Failed!" if re.search(reg, string) is None \
        else "Word Matches the condition"


def main():
    string = input("Please enter a word: ").strip()
    print("Status: ", matching_seq(string))


main()
