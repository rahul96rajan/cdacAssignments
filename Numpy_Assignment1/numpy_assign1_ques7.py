'''Write a NumPy program to test element-wise for NaN of a given array.'''
import numpy


if __name__ == "__main__":
    arr = numpy.array([0, 1, numpy.inf, numpy.nan])
    print("Array : ", arr)
    print("NAN Status of Array : ", numpy.isnan(arr))
