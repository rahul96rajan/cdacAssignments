'''Write a NumPy program to test if any of the elements of a given array
is non-zero.'''

import numpy


if __name__ == "__main__":
    arr_without_zero = numpy.array([-1, 1, 2, 3, 5, 6])
    arr_with_zero = numpy.array([0, 1, 2, 3, 5, 6])
    print("1st Array :", arr_without_zero)
    print("2nd Array :", arr_with_zero)
    print("Is the only non-zero elements in 1st Array: ",
          0 not in arr_without_zero)
    print("Is the only non-zero elements in 2nd Array: ",
          0 not in arr_with_zero)
