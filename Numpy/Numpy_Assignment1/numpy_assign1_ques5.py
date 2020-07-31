'''Write a NumPy program to test a given array element-wise for finiteness
(not infinity or not a Number).'''

import numpy

if __name__ == "__main__":
    arr_without_inf_or_nan = numpy.array([-1, 1, 2, 3, 5, 6])
    arr_with_inf_or_nan = numpy.array([0, 1, 2, 3, 5, 6, numpy.nan, numpy.inf])
    print("1st Array :", arr_without_inf_or_nan)
    print("2nd Array :", arr_with_inf_or_nan)
    print("Finiteness of Array 1 : ", numpy.isfinite(arr_without_inf_or_nan))
    print("Finiteness of Array 2 : ", numpy.isfinite(arr_with_inf_or_nan))
