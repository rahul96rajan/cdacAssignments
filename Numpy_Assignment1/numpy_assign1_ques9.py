'''Write a NumPy program to create an element-wise comparison
(greater, greater_equal, less and less_equal) of two given arrays.'''
import numpy


if __name__ == "__main__":
    arr1 = numpy.array([0, 1, 2, 3, 4,  numpy.inf])
    arr2 = numpy.array([-1, 3, 2, 2, 5,  numpy.inf])
    print("Array 1 : ", arr1)
    print("Array 2 : ", arr2)
    print("Is Array 1 greater than 2 :", numpy.greater(arr1, arr2))
    print("Is Array 1 greater than or equal to 2: ",
          numpy.greater_equal(arr1, arr2))
    print("Is Array 1 less than or equal to 2: ", numpy.less_equal(arr1, arr2))

    print(numpy.less_equal(numpy.array([numpy.nan]), numpy.array([numpy.nan])))
