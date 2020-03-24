"""Q6: Write a Python program to display the Fibonacci sequence up to
 n-th term using recursive functions"""
from question2 import input_positive_integer


def fibonacci_series(lim, a=0, b=1):
    print(a+b, end=", ")
    if(lim-1 > 0):
        fibonacci_series(lim-1, b, a+b)


if __name__ == '__main__':
    num = input_positive_integer("Please input the limiting factor: ") - 2
    print("-"*40 + "\n" + "-- Fibonacci Series --")
    print("0, 1, ", end="")
    fibonacci_series(num)
    print("\n" + "-"*40)
