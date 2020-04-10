'''Write a NumPy program to test whether none of the elements of a given array
is zero.'''

import numpy


if __name__ == "__main__":
    arr_without_zero = numpy.array([1, 2, 3, 5, 6])
    arr_with_zero = numpy.array([0, 1, 2, 3, 5, 6])
    print("1st Array :", arr_without_zero)
    print("2nd Array :", arr_with_zero)
    print("Is zero in 1st Array: ", 0 in arr_without_zero)
    print("Is zero in 2nd Array: ", 0 in arr_with_zero)
