# Q19. Write a Python program to find all
# words starting with 'a' or 'e' in a given string.
import re


def a_e_strings(string):
    ae_reg = re.compile(r"^[a|e]\w+")
    words = [x.strip().strip(".") for x in string.split(" ")]
    return list(filter(lambda x: re.match(ae_reg, x) is not None, words))


def main():
    string = input("Please input a string : ")
    print(a_e_strings(string))


main()
