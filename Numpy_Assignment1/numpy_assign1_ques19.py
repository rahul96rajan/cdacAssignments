'''Write a NumPy program to create a 3x4 matrix filled with values ​​from
10 to 21.'''
import numpy

if __name__ == "__main__":
    print("Random Array : \n", numpy.arange(10, 22, dtype=numpy.int8)
          .reshape(3, 4))
