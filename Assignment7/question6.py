# Q6. Write a Python program to remove everything except
# alphanumeric characters from a string.
import re


def replace_string(string):
    reg = re.compile(r"\W")
    return re.sub(reg, "", string)


def main():
    string = input("Please input a string : ")
    print("Replaced String : ", replace_string(string))


main()
