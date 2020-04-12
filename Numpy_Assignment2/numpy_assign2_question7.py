'''Write a NumPy program to check two random arrays are equal or not'''
import numpy

if __name__ == "__main__":
    arr1 = (10*numpy.random.random([2,1])).astype('int8')
    print("Array1: \n", arr1)
    arr2 = (10*numpy.random.random([2,2])).astype('int8')
    print("Array2: \n", arr2)
    print("\nAre two arrays same?", numpy.allclose(arr1, arr2))
