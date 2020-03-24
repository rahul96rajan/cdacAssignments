'''Q8: Write a Python program to convert decimal number into binary number
 using recursive function.'''
from question2 import input_positive_integer


def decimal_to_binary(num):
    if num == 0:
        return 0
    else:
        return num % 2 + (decimal_to_binary(num//2) * 10)


if __name__ == '__main__':
    num = input_positive_integer("Please input a integer: ")
    print("-"*50)
    print("Binary equivalent of"
          " '{0}' is '{1}'".format(num, decimal_to_binary(num)))
    print("-"*50)
