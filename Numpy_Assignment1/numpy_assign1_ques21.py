'''Write a NumPy program to compute sum of all elements, sum of each column
and sum of each row of an given array.'''
import numpy

if __name__ == "__main__":
    matrix = (numpy.random.random([3, 3]) * 10).astype(numpy.int8)
    print("The Matrix generated:\n", matrix)
    print("Sum of all elements :", numpy.sum(matrix))
    print("Sum of all columms :", numpy.sum(matrix, axis=0))
    print("Sum of all row :", numpy.sum(matrix, axis=1))
