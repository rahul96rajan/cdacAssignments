'''Write a NumPy program to create an array of 10 zeros, an array of 10 ones,
and an array of 10 fives.'''
import numpy


if __name__ == "__main__":
    arr_zeros = numpy.zeros((5, 2), dtype='i')
    arr_ones = numpy.ones(10, dtype='i')
    arr_fives = 5*arr_ones
    print("Array of 10 ones : ", arr_ones)
    print("Array of 10 fives : ", arr_fives)
    print("Array of 10 zeroes : ", arr_zeros)
