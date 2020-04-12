'''Write a NumPy program to reverse an array (first element becomes last).'''
import numpy

if __name__ == "__main__":
    arr = numpy.arange(1, 11)
    print("Array :", arr)
    print("Reversed Array :", arr[::-1])
