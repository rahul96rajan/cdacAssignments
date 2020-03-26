'''Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9'''
# from sys import path
from sys import path
path.append("/home/rahulrajan/Documents/dev/scripts/cdacAssignments/"
            "Assignment11")


def odd_sqaured(lst):
    return ','.join([str(x**2) for x in lst if x % 2 != 0])


def main():
    from question11_2 import get_int_tuple
    input_tup = get_int_tuple(input("Please enter values(comma-separated):"))
    print("Squared odd numbers are: ", odd_sqaured(input_tup))


if __name__ == "__main__":
    main()
