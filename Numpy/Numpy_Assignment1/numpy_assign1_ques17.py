'''Write a NumPy program to create a vector of length 10 with values evenly
distributed between 5 and 50.'''
import numpy

if __name__ == "__main__":
    print("Random Array : ", numpy.linspace(5, 50, num=10, endpoint=True))
