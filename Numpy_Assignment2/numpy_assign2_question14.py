'''Write a numpy program to swap two columns in a 2d numpy array?'''
import numpy

if __name__ == "__main__":
    arr = (10*numpy.random.random([4, 4])).astype('int8')
    print("Array before swapping:\n", arr)
    arr.T[[0, -1]] = arr.T[[-1, 0]]
    print("Array after swapping:\n", arr)
