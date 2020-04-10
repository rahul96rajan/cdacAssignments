'''Write a NumPy program to create a vector with values ​​ranging from 15 to
55 and print all values ​​except the first and last.'''
import numpy

if __name__ == "__main__":
    arr = numpy.arange(15, 56)
    print("Array (15 to 55) :", arr)
    print("Array (without first and last values): ", arr[1:-1])
