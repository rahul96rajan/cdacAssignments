'''Write a NumPy program to append values to the end of an array.   '''
import numpy

if __name__ == "__main__":
    arr = numpy.ones((10, 10), dtype=numpy.int8)
    arr_jr = numpy.zeros((2, 10), dtype=numpy.int8)
    print("Array: ", arr)
    print("Array Jr: ", arr_jr)
    print("Fused Array :\n", numpy.append(arr, arr_jr).reshape(12, 10))
