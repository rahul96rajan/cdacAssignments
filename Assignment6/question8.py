# Q8. Write a Python program that matches a
# string that has an 'a' followed by anything, ending in 'b'.

import re


def matching_seq(string):
    reg = re.compile(r"(^a|\s).*b(\s|.)")
    return [x.group() for x in re.finditer(reg, string)]


def main():
    string = input("Please enter a sentence: ").strip()
    print("Matching Sequences : ", matching_seq(string))


main()
