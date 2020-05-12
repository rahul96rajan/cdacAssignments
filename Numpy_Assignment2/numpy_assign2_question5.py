'''Write a NumPy program to compute the median of flattened given array.'''
import numpy

if __name__ == "__main__":
    arr = numpy.random.random([3, 3])
    print("Array: \n", arr)
    arr = arr.flatten("F")
    print("\nArray Flattened: \n", arr)
    print("\nMedian of flattened array:", numpy.median(arr))
