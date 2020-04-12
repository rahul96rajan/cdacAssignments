'''Write a NumPy program to add, subtract, multiply, divide arguments
element-wise.'''
import numpy

if __name__ == "__main__":
    # random_num + 1 b/c else zero would be produced causing num/0 valueerror
    arr1 = (10*numpy.random.random([5])+1).astype('int8')
    arr2 = (10*numpy.random.random([5])+1).astype('int8')
    print("Array 1: ", arr1)
    print("Array 2: ", arr2)
    print("Array 1 + Array 2: ", arr1 + arr2)
    print("Array 1 - Array 2: ", arr1 - arr2)
    print("Array 1 * Array 2: ", arr1 * arr2)
    print("Array 1 / Array 2: ", (arr1 / arr2).astype('float16'))
