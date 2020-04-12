'''Write a numpy program to reverse the rows of a 2D array?'''
import numpy

if __name__ == "__main__":
    arr = (10*numpy.random.random([5, 5])).astype('int8')
    print("Array before reversing columns:\n", arr)
    i = 0
    length = arr.shape[0]
    while(i <= int(length/2)-1):
        arr.T[[i, length-1-i]] = arr.T[[length-1-i, i]]
        i += 1
    print("Array after reversing columns:\n", arr)
