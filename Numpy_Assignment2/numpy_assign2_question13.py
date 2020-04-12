'''Convert a 1D array to a 2D array with 2 rows'''
import numpy

if __name__ == "__main__":
    arr = (10*numpy.random.random(5)).astype('int8')
    print("Array before resizing: ", arr)
    print("Array after resizing:\n", numpy.resize(arr, (2, 2)))
    arr = numpy.delete(arr, -1, axis=0)  # deleting last elem
    print("Array after reshaping:\n", numpy.reshape(arr, (2, 2)))
