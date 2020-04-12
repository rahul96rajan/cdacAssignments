'''Write a NumPy program to Replace all odd numbers in arr with -1'''
import numpy

if __name__ == "__main__":
    arr1 = (10*numpy.random.random(10)).astype('int8')
    print("Array before replacement:\n", arr1)
    arr1[arr1 % 2 != 0] = -1
    print("Array after replacement:\n", arr1)
