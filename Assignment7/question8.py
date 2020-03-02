# Q8.  Write a Python program to check a decimal with a precision of 2.
import re


def input_float(msg):
    try:
        num = float(input(msg).strip())
    except ValueError:
        print("Please input float values only!")
        num = float(input(msg))
    return str(num)


def precision_of_2(string):
    reg = re.compile(r"(^\d+|^).?\d{2}$")
    match = re.match(reg, string)
    if match is None:
        return string + " does not exactlty have precision of 2"
    else:
        return string + " exactlty have precision of 2"


def main():
    string = input_float("Please input a decimal value : ")
    print(precision_of_2(string))


main()
