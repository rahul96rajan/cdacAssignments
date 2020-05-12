'''Write a NumPy program to create a 5x5 zero matrix with elements on the main
diagonal equal to 1, 2, 3, 4, 5.'''
import numpy

if __name__ == "__main__":
    print("(1 to 5) Diagonal Matrix :\n", numpy.arange(1, 6)*numpy.identity(5))
    # numpy.diag([1, 2, 3, 4, 5])
