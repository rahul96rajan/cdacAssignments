'''Q7: Write a Python program to find the sum of natural numbers up to n
 using recursive function'''
from question2 import input_positive_integer


def sum_of_series(lim, a=1):
    if(lim-1 > 0):
        return a + sum_of_series(lim-1, a+1)
    else:
        return a


if __name__ == '__main__':
    num = input_positive_integer("Please input the limiting factor: ")
    print("-"*50)
    print("Sum of all natural numbers till"
          " '{0}' is '{1}'".format(num, sum_of_series(num)))
    print("-"*50)

# maximum recursion limit at number 998
