# Q4. Write a Python program to find all three, four, five characters
# long words in a string.
import re


def fetch_string(string):
    reg = re.compile(r"\b\w{3,5}\b")
    return re.findall(reg, string)


def main():
    string = input("Please input a string : ")
    print("[3, 5] letter words in the string are :\n =>", fetch_string(string))


main()
