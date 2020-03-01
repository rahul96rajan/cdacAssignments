# Q9. Write a Python program that matches
# a word containing 'z', not at the start or end of the word.

import re


def matching_seq(string):
    reg = re.compile(r"^[a-yA-Y]+\w*z\w*[a-yA-Y]$")
    str_list = map(lambda x: x.strip(), string.split(" "))
    return list(filter(reg.match, str_list))


def main():
    string = input("Please enter a sentence: ").strip()
    print("Matching Sequences : ", matching_seq(string))


main()
