# Q4: Write a Python Program to find the factors of a number

from question2 import input_positive_integer
import time


def factors(num):
    i = 1
    lst = []
    head = i
    tail = num
    while i <= num:
        head = i
        if tail <= head:
            break
        if num % i == 0:
            tail = num/i
            lst.append(i)
            lst.append(tail)
        i += 1
    return lst


if __name__ == "__main__":
    num = input_positive_integer("Enter any positive integer : ")
    start_time = time.time()
    print("Factors of '{0}' are {1}".format(num, factors(num)))
    print("Time Taken is '%s' Seconds" % (time.time() - start_time))
