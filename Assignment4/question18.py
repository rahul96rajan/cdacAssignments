# Q18. Write a program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

import re


def string_to_sorted_(string):
    return " ".join(str(x) for x in sorted(set(re.split("\s+", string))))


def main():
    string = input("Please enter a sentence with spaces : ")
    print("Output : ", string_to_sorted_(string))


main()
