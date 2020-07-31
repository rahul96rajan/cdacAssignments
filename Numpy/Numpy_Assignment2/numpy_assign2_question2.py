'''Write a NumPy program to extract all odd numbers from an array.'''
import numpy

if __name__ == "__main__":
    arr = numpy.arange(1, 11)
    print("Array :", arr)
    print("Extracted Odd Array :", numpy.array(
        list(filter(lambda x: x % 2 != 0, arr))))
