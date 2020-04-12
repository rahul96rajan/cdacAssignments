'''Write a NumPy program to compute the multiplication of two given
matrixes.'''
# didn't used matrix class as it was depricated.

import numpy

if __name__ == "__main__":
    arr1 = (10*numpy.random.random([2, 2])).astype('int8')
    arr2 = (10*numpy.random.random([2, 2])).astype('int8')
    print("Matrix 1:\n", arr1)
    print("Matrix 2:\n", arr2)
    print("Matrix1 x Matrix2:\n", numpy.dot(arr1, arr2))
