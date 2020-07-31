# Q3: Write a Python program to find the H.C.F of two input number
from question2 import input_positive_integer


def euclidean_algo_hcf(a, b):
    if a < b:
        a, b = b, a
    rem = a % b
    if rem != 0:
        return euclidean_algo_hcf(b, rem)
    else:
        return b


if __name__ == "__main__":
    num1 = input_positive_integer("Input number 1 : ")
    num2 = input_positive_integer("Input number 2 : ")
    print("HCF of {0} and {1} : {2}".format(num1, num2,
                                            euclidean_algo_hcf(num1, num2)))
