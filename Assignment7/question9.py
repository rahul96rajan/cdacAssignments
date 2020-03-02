# Q9. Write a python program to replace all html tags
# by the space in the given string.
# For example:
# Input String: “<html> This is a python regular expression. </html>”
# Output String:  This is a python regular expression.
import re


def replace_string(string):
    reg = re.compile(r"<.+?>")
    return re.sub(reg, " ", string)


def main():
    string = input("Please input a string : ")
    print("Replaced String :", replace_string(string))


main()
