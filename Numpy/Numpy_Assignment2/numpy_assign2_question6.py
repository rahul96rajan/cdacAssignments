'''Write a NumPy program to find the most frequent value in an array.'''
import numpy

if __name__ == "__main__":
    arr = (10*numpy.random.random(10)).astype('int8')
    print("Array: \n", arr)
    print("\nMost common of array:", numpy.argmax(numpy.bincount(arr)))
