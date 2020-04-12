'''Write a NumPy program to get the powers of an array values element-wise.'''
import numpy

if __name__ == "__main__":
    arr1 = (10*numpy.random.random([10])).astype('int8')
    print("Array1: \n", arr1)
    print("\nArray of Array1 elements raised to 2", numpy.power(arr1, 2))
