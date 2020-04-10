'''Write a NumPy program to test element-wise for complex number, real number
of a given array. Also test if a given number is a scalar type or not.'''
import numpy


if __name__ == "__main__":
    arr = numpy.array([0, 1, numpy.inf, numpy.nan, 3+4j])
    num = numpy.complex128(5+8j)
    print(num, num.dtype)
    print("Array : ", arr)
    print("IsComplex : ", numpy.iscomplex(arr))
    print("IsReal Status : ", numpy.isreal(arr))
    print("IsScalar Status : ", numpy.isscalar(arr))
    print("IsScalar on number : ", numpy.isscalar(num))
