'''Write a NumPy program to create a 2d array with 1 on the border and
0 inside.'''
import numpy

if __name__ == "__main__":
    arr = numpy.ones((10, 10))
    arr[1:-1, 1:-1] = 0
    print("Array :", arr)
