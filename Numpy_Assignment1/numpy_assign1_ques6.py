'''Write a NumPy program to test element-wise for positive or negative
infinity.'''

import numpy


if __name__ == "__main__":
    arr = numpy.array([-0.0, 1, 0.0])
    print("Array before division : ", arr)
    arr = 1/arr  # to get a negative and a positive infinity
    print("Array after division : ", arr)
    print("Finiteness of Array : ", numpy.isinf(arr))
