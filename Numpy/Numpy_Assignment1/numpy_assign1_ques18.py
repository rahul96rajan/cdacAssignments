'''Write a NumPy program to multiply the values ​​of two given vectors.'''
import numpy

if __name__ == "__main__":
    vec1 = numpy.arange(0, 5)
    vec2 = vec1+1
    print("Vector 1 :", vec1)
    print("Vector 2 :", vec2)
    print("Product of Vector 1 and 2 :", vec1*vec2)
